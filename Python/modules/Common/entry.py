from Common import *



from typing import Union, List

def entry(returnType: Union[type[str], type[char], type[int], type[float], type[bool]],
          errorMsg: str = "please retry again, the type needed is :",
          blackList: List[str] = ["isspace()"],
          whiteList: List[str] = None):
    """
    # entry
    returnType -> str, char, int, float, bool
    failureMsg -> "please type again, the type needed is :" -> auto complete after ':'
    blackList -> illegal char, "isspace()"*(all space or void)
    whiteList -> None
    """
    def is_blackListed(input: str, blackList: List[str]) -> bool:
        for key in blackList:
            if key == input.lower():
                return True
            elif key == "isspace()":
                if buffInput.isspace() == True:
                    return True
        return False

    def is_whiteListed(input: str, whiteList: List[str]):
        for key in whiteList:
            if key == input.lower():
                return True
        return False

    def tryAgain():
        print(errorMsg, returnType)

    while True:
        buffInput = input()
        if whiteList != None:
            if not is_whiteListed(buffInput, whiteList):
                tryAgain()
                continue
        if is_blackListed(buffInput, blackList):
            tryAgain()
            continue

        if returnType == bool:
            if buffInput.lower() == "yes" or buffInput.lower() == "y" or buffInput.lower() == "oui":
                return True
            elif buffInput.lower() == "no" or buffInput.lower() == "n" or buffInput.lower() == "non":
                return False
            else:
                tryAgain()
                continue
        else:
            try:
                return returnType(buffInput)
            except:
                tryAgain()
                continue