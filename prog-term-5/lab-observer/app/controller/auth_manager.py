from app.tools.singleton import Singleton
from .. import app_logger, socketio
from time import time, sleep
from abc import ABC, abstractmethod

import asyncio

logger = app_logger.logger

class AuthException(Exception):
    pass


class SessionInterface(ABC):

    @abstractmethod
    async def lifecylce(self):
        pass

    @abstractmethod
    def notify(self):
        pass


class SessionObserverInterface(ABC):

    @abstractmethod
    def update(self, session: SessionInterface):
        pass


class SessionObserver(SessionObserverInterface):

    def update(self, session: SessionInterface):
        socketio.emit('AuthNotification', {'message': 'It is time to fetch rates again!'}, to=session.session_id)


class Session(SessionInterface):
    _observer: SessionObserverInterface

    def __init__(self, session_id, updated_at, ttn=10, observer = None): # ttn - time to notify (In seconds)

        self._observer = observer
        self.updated_at = updated_at
        self.ttn = ttn
        self.session_id = session_id

        self.cycle = asyncio.run(self.lifecylce())
    

    async def lifecylce(self):
        sleep(self.ttn)
        self.updated_at = time()
        self._observer.update(self)


    def notify():
        self._observer.update()


class AuthManager(metaclass = Singleton):
    # Primitive login system cuz i'm lazy
    AuthData = {} # Login + Password
    SessionData = {} # Login + Session

    _SessionObserver = SessionObserver()

    def __init__(self):
        super().__init__()
    

    def register_user(self, login, password):
        if self.login_exists(login):
            raise AuthException("login occupied")
            return False

        self.AuthData[login] = password
    

    def login_exists(self, login):
        existingLogins = list(self.AuthData.keys())
        if login not in existingLogins:
            logger.warning(f"login {login} is missing in AuthData")
            return False
        return True


    def is_login_in_session(self, login):
        existingLogins = list(self.SessionData.keys())
        if login not in existingLogins:
            return False
        return True


    def auth_check(self, login, password):
        print(self.AuthData) 
        if not self.login_exists(login):
            raise AuthException("Unknown login")
            return False
        if self.AuthData[login] != password:
            raise AuthException("Wrong password provided")
            return False
        
        return True


    def login_user(self, login, password, session_id):
        if not self.auth_check(login, password):
            raise

        if self.is_login_in_session(login):
            raise AuthException("User already in session")

        self.SessionData[login] = Session(session_id, time(), observer=self._SessionObserver)

        return True
    

    def logout_user(self, login, password, session_id):
        if not self.auth_check(login, password):
            raise
        if self.is_login_in_session(self, login):
            del self.SessionData[login]
            logger.info(f"{login} logged out of session {session_id}")
            return True

        logger.info(f"{login} has no assosiated session")
        return False


    def delete_user(self, login, password):
        if not self.auth_check(login, password):
            raise
        if self.logout_user():
            del AuthData[login]
            return True

        return False
