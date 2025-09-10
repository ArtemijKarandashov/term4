from HTTPLoader import url_hook
import sys

sys.path.append("http://localhost:8000")

import myremotemodule
myremotemodule.myfoo()
print(myremotemodule.myfoo)