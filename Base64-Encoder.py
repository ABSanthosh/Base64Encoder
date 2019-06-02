import base64
import os
import tkinter
from tkinter import *
from tkinter import PhotoImage, filedialog, messagebox

import pyperclip

top = tkinter.Tk()
top.title("Base64-Encoder")


def select():
    global strr
    filename=filedialog.askopenfilename()
    fpath= os.path.split(filename)[0]+"/"+os.path.split(filename)[1]
    with open(fpath, "rb") as imageFile:
        strr = base64.b64encode(imageFile.read())
    convert2.config(state='normal')

def copytoclipboard():
    global strr
    pyperclip.copy(str(strr))
    messagebox.showinfo("Copied","copied to clipboard")

def quit1():
    top.destroy()

def reset():
    filename=None
    convert2.config(state="disabled")

dats ='''R0lGODlhCgFmAXAAACH5BAEAAIsALAAAAAAKAWYBhwAAAOhMPdtHOeFJOt5IOuhLPNlGOOlLPOdKO+BJOnlLR+RKO9pHOdxHOOhIOeo+Luw0IuYtHOUzIuhdUOhsYet7cOKUjPCQh/CgmOWDeegpF9+lnty+utrb2u/v8Ob9/vT///Ly8vvS0PW7tvHl49jj4tvLx9+0r9bX1dbz9Nb7/Pr6+vT19dbr6/XMx+bm5uPj4////56dnl5dXUZGRispKyAgIHBwcbGxsXx7fVFOUDY3NlZUVMTExBUUFWdmZUxLTZKRkj8+P4aFhczMzaqnqLu7u/OrpDQxM+hVRu1NPvJOPtFFN8VANLo8MLM6L6w9M/9PO1Npd2w9PpBFQn+jrp+vtzBKVv7l4f7y7wMtRv/a1w8zRwAOJgAmO0FYaH2PmQAaMml/ix07Tubl5Mywsf/Mydzd3ebp6ebo6JeVhdTOx+Hh4eDi4Obn5+Xf3qGWhqWgjkJBQkVERUZFRktNTUlKSkxISkhKSklHSEtISk1LTEFBQEVERDY4NjI2MzM1MzM4Nhk0Njg7NqinlKKij6KikLCwnKCgjoODdJmZhwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAj/ABcJHEiwoMGDCBMqXMiw4cIGDwg4nEixosWLGDNq3Mixo0eBSR4kSaLko8mTKFOqXMmSYgMlSRqETNKyps2bOHOynClSCQGaOoMKHUo0aBICMEWKlFi0qdOnUCnOlKkUaNSrWLMSTTrzp5KSWsOKHXsS6cyvLyGSXcu2bUOuVGdadUu37toGcXv+FGm3r1+sBB58PerzK8y/iBMPhYm0Z2GkiiNLNqmEL8HCMXmGbDC5s+eJZqtyFohUyUufJPd+Xk33Ad7KUjeTJPlVINqvpUuHZM1bLESSPUWqVVh5pHDhsBfhvm0abe/nV82aJilzsOu5BGW+DGkdJufXhcPL/yTo+iX08znTfhU9vepBzUh/vuSrOe/RgZofoN/PskFpmaFx1xV32Q0W4FIlLVUfbQKddhR1/EV4UlWizeaYgjEN5N9tXuEWF2rrxQRWWhSOJuGJG3lnIXyoUWiabc0Z9lJueWEmGE2BwcQVdij2WNFUuHVlmFdmnTaaeqcVNmNqU4UkEYDCTeXjlBYlFV6TFHIXo2lJxqekk9bJtUhgxolH5ZkTVYfUdlURmdpy/m1Y2pCcvUlke9TRtiaafDY043KELYfnnOF5WdoiLs6JF08xmtjnowhtGOOazO0loqXIKQliZsK95qZwkIaakJGCHpjfg1EiiKeqhVrnqKiw4v+3ZJaMMWlYi9TdpheQ4uHa6XCxiuoaYyoKlmRaWrZa7K3/sajZVIEF+yh4jb056WDIsqdXfJrhCmKIhk1lmbQREkBmll4+htapmL654JVKNVcdnmG6Ri50EQXp5pBnqavgrTq26yuQnwKJHJvAZXhvZ1fap5R99nWoKcTWhplkeLXeyJWCjqW2cGLzVqvXt3dOZ9jB7J76Z323/bZUlIWKK+7HdB0VL7cjy3iqsQMjSJiQqBJm6WlzrqhlqlbK1dOrNGeV8IC7shckiJZ6265jW85p6sG4yudsgD6JFJN+TV+lnXctDglos1lyDLTb6g3a6oO58RtvuKE9JqCA45b/TdTVZwnNcptUdytwkG0nnOl8uU7KZNzbad3th34L1dPbnDrrs26EV0zYn5iZ5WXQPi+eX6+N8s0pV0xVfpPAqQ44MG7stftnl6WWajiLGO+rLNE/V+Vr666rJBPUgRrIXOgYiwiw8+KxvCrmpWvpsJDT8yy66iPxWDxHtF0YdNyNLjfyuZeWH3PihcOsdmbVtp+yjgNjWhzT32fkqWyWEgp63cUKVKC25rzq/OxqG1vT6QLYObPw5H8boxtPiJc/iwiGXyEKTvpyp6lWEU1vPRsbfGxlwK49rk1MolCR9PQ+b20KfxVkSHVq5BURJW966VKWuiK4ObzxMD9JOt1sCwAoO0YZaYK3uh7Z/2LYkHZ96j/3i9mWZmUnGRXOijvklgnFhpx9uSx9mNKiE2cDOm+BiokPoV6/OLezzEmNbdyBY+IAuBfW9U5QN2TjDw90rN0tBY0JSdj9kPfBB8nvX0ND3BArZSvA7QpnvPrgG1GDrG+BMIueOyMgybMdAAFKVQrkWXuUx6g9XquNoiPW9QgIt3XdjTlx4x0U5cWVTQrkcuy7XnEEhSAUfulbUlMTiNg3tartq2rzo9T6LtXGxPWNiexSpQ9tmK7+Eas5s1xZNm10QGkSMV4fjGAqPxlJcRLrgN2cDSAbqTgWHouRuGxmNHWYRUH97pBYShipsNlO4WERion7DTTniP+2PjozV6lEZ8Zocy11AXCfcrzSOGdIGyWm00tHrNA5qwbDponRWujL1DF5pUxSCU+EEFNkSrGJQUeqjF8FoxXgwogWwhGgowsLKZgwYyB5gpJZeOQaowJFlY1dE2PZQ17/uGPRhDrxqIG7HBspSDOxIbNQmbpiTKt4LYFtVWwIq1tcusTOnJ1lqWYsYHE4yiGCFSd2S2xaBKlSN7VOCl0MzGf1BFPXvOEqYhzioKA8WTS+hmmWHaIjvIBmTe+RS3DgsmtDR4quFFoWkdLz5Oxc2kVlOYZSiXRpOLV2ycJgjUwevSA/ixq9BzwAArCVgAY0IFsNREADEBgWUZNVtJn/8tCepLvoXIG0QdJWRgIQkEAElMtc3ObWtYb6ZFzguBmajaSMhDPNa3M7AQpUwAIWuAAGxouBC1yAAhN4AG3xOlYUfjaAiTxpljLarfkuJzC0JQAFMiBe8mLAAhvIAHpDogHXnkqRrerJx8g3nXQ1ALYPyMAJOHAGFqgABBjOsIZZsAUMVEC91zHnOZd24OYArcEZA+5ZR8wp3E7gAiPwgIZnDIIYqKAFJjjBBiYAgQIbcKWjA9DCpOeYB0OAAic4QwpUoIIY1JgFLJCxB6IMAhlr2AwXeG2+3Gg4Vz7uvjKrrGgUBMH1SEACFBjBjD0g5SmzGcoxcDKTYcCBDGxX/3Ihwp1S7hU5FgUGAhPgQAsGzeYYRJnNiE60ojPsgQuc+WtoG5Q8e8vihL4Sq4B2AaMVnehDIzoLMfDAoFVgAjtDIC+aNVRFydW7N4H4BCpIwRkqHOpPR/nWbua0lUEwAhD/kFZrZWee36rXJlGSpcu9wKbdnIVDU1nXHgB1C87QAhWggAIFHmbFAistJgTWtBE+gwqIcAYP1PrNuXYzrqGc7l072sCpnChRYclNS6dTlA5S7wQ0XWVE43rKWfh0odE9cBig4MYnIAAEOBjKrgRrxaXJrQlujIIz1Prfb46zxuPs73ZbeQSPFp4y47dP4L0XqXSsz2uVjWF0r9vcG/93cscTDWoPEKENKjgDtkfbrZnEypMXO/XBZ23xlwcc5nFuQ8WRHoOAR/nobMawC6C7Q3W91JyIVRallSABls/80Bv3ANGZjmgQQD3UKDi4CiqgAfrGmzGw6ldaFi5uIizd2ehOugx4AAgb2MAHNujDD2Rg8Yu3m9cFZiFpfYecNbKsmnBSigYm0HKXFzrORchBH/rud0DwIAdG0Hii+x2DWROh2hnI7VkCChZIubUyEOCAtc9ABHOz2ekwR0EOfACA3vvg97z3/QzawHG8WzkDbfczFldWIfdiL7o6enCb/82COMvABr33/e+zD4A+FIHjnC59xavNdopulCehchj/ATRggdmjgPiWj3MOfO/3+tv/7wDwwRDA/28QsOC1JZNIyzRGu5JnKqNeajZ9l9cDNdB79/eAvdcHhadrtIcC05ZbzYEcIudYU3JBPwMBGaACJXAGFXdubhYDRIB9gOd3weeA99d7gIAChkZw5vYGuYUwPzU3PVQv05EsqKIEEOB1BBdnP+CC9teCAGB/vZcI/Id7FXdwJvBaPzgvcQEpf9ITgDZoaYcC6naCZ+CCgJeEM5ADOQAI+QeBAEAEoYZ7MhYDyAdC87Ug9qUmytciDVB5uRZnfXCGL+gDY1iGfIh/OTCDuFZ6RKcCFqAB4fJt8vEoZLIXDwZraTdroeZp/4bGe0rIA0w3BIFYf/lncTQIAlswLDqzUDdCKHakNnaUHxqgbAIHczyQhBAICIWHeb9Xf7z3fcbnAZNogTwmG870KMaRGkeWc0+Ya82mhwBQA57YBzFnfbJofw3ojIYXdWynKZnyfCwlPZCESK6lgFEWA0YQjUpIjTFXBOTYe/C3brOWdiqwAaeWJ/LzKDeiFLHXAk9YYf8WAzhAjthXizG3hw/Iez1QidEWdSOgAeliRMNoU3ozR0gkARVgdl0YZ2b4gP/4jMqohDpQfIWGj+3YAulVcoAijNKRhSRIgi1geHHWgOWokdCIkQDAA/w3ZVVmYI3nFTDTIQUIQhJTQ/9foQFH0G+WiI4yaY7PKAP+mIaGF3BbeHCJGFA+xydFYhoQsAGzR4IHCXZGmYkwGQNdeX+8p4b9BwIUIAG7ZVib0VZFNVpeNiyB0QBmUGWFGAMCCYE0CZNh6Xcz2XSWmJLUhgJrxWJ7hiaM41oPYAIguXQuFwOxKJY28JXzh5G8N4iheAGJt4HxJFMrljo6ohSUR5SFRgSd6Ik1IJn++Hu252ltkJIHVwGqRysxQVU94klJcGTTlo/7GAMX+YJqoJEecIsyiQdN14UgcAQRcE4Io02EWUA7Ux0SQHkvFwNKiZF8GQQwKZxK+H3qlgWLqWTwmE5tySeaAYLu934siQL/2omLTBl22Ged2AcIcdZ/IPdF/mRa7wJA8tMcEkmXeZcI/niEAPB9ARmg2CcDhChjb1BxJJgCHBCb5oMq5PkfENB+DDprHRcD6rmCfZgDPTBrMsB7zGidgLeS68ZrEuCBqRRL4zSYq5IbUyEBGdByRxdnN2Cg7PkD5IYCMtCbELh/yGhzKYljTlJFAkKeCHKVspaPBll9G4qRNRB827eM8Pl3NWB76oai8vFPcEJv83NWMwEBExl/RVilfJl/wQefALB/uAYCREeCaZdeA7gbaLIxSpqPFZaHHvB3HEqZfaqmgFBzbQpylVEp95U7o3MgX1KP/cluYMeJZoqLfwqB/wjabpNIbWcgp/U2GGiCSErajnfHbHaJo5EKgT8wg1uJoqlmTw11XwX4k3kio/5XkeNYqrbKlOiWBYA5iRMgAYrVHGiSH1eZmyk5ZYdWYwBqq5G6pglKZScgAYUKfWWWQ3aVLTGiARPpqAO3nsoKgTZgbixwdG6aj/ioqaPjHmdyPhBwAiAJp11obj1Aqt2qmtXIAiCwARGQWG1EKgL4q0NTjIZXfTGgA/KqrABgmQS3q7OWXnUjRsEaIBqAlfn4fs2GaBvZrTJ5quHanYgIAcCITvOyWBcEUUE1E+uYaOJYsKXKezLYnbxIrigAJoU1lVSCQhU6ba5ZbtqaspM6r6UAAIoVqQKphzVRFEwmM0CDBWYGdgaiGY6jirEQeAPNOq5EZ4Em8BvqQodociAoyaBp1wJsWH3VCbWeyKZdGK4i6bGg5YN1pCgshTrhFBLr2mRPZ7EeYIRQCwDyaZBuBqcpmQLw+Gs0OyVTUxwW6JoVV7Fg55gqa53dB37qZmMPajdklIHjAzBehai32X6452zUWZq36gNYeoJK146z1gKptyRUgxr/fPIwR7Gu30mCJ3t5d9mtj3tuePeO8dh8ApRd1lqVOPQVWbia6fa5jVt/DQgAoedyTomnvrhwqsg55PmZSaABIVi1xYpxyni8vTeIAQtwbZC2UaUyllVILmU7idkCZ3t5RYCJK5uEanh7XjixB3cCCilCi3MYhgkmt9kAKDCCE9sGzbab10d/lOmABGp55jZoUTiY05VibERQ3dRT6tV+AsxsFhtqsWjAYpl9P0C8YPeyeCq0sbkit4Ok1yUS7Od+rrmSNMhxQ9AH2Md92Rd4+1eTtxZlSpZ6ERRCcFJWLNQr9vkAbVACLoxxMGcEOoB/NJx/gKCjkJvDL4u4OKZ6/94hPlzCJ2kDHBBggb0IpwJ8a2fHcUUgAzlwAzeQA0FgBEinaIcWcNT2oA/cPCt0UAhCsoOhItZrbQcJcCircUQgA0OAxjcwBDKghqK3lW72xQyqAhSwu9thYklClUHyG3tsuk/IhYqbawL7lXy7bqF2Bm2QArfZSpbrS5R1dWtSFbBlAimAAtWnwJfnyZ2mbizAyCSoAvZbFeUErPvrXhogiV4Lxqi6sbrmf1C3vhvrjoloISi3UdELXPZWPTLhsfiInuuWzHZLkboWjlM8sS3QBhBhitPTJ1gbIoHxAEo2sX4by+9at2XXx7jWbNf8yjcYT9lydSQJUX40Eys8if/ujHEVW8tZUGWKywJKx84VlwLYBj0FA3d8AnQr4rEpcM05W3FtYG5EKa59rMDVxwJwWm2PjEvne00kS1oj1DmuAQETt4VTVsycvL7+ZmgJfdHihq/gRL7P1IEqRx17HLuZnNHGinFE7c6t+bUpwHYJIELGdFldNj1HZDWncmri5rdvpq3Gt7hsVtPDXHHjVsLFFD4MMqELxRPYmgKv7Lx+W25uRpFVZnbcfNSTWNETkHwaQ8GQxmVuwz6oiCqwJXtPKcpX7c1ufXSg2tWyq8uZ6UbNokDCKHLFEgETUG2Ii7iTmNFsjWjldtiTaG3VWxwotUtftTst1UgOpUwxAVv/WFm6WyjKJKC+idYGJMDZNm2BiJht9hEw4BIRjwIXB9Z2E8fVgMnZvfiUzqvL6jUdWIs8Kt1NUOSvh3VYF6ReGaCFlp12O2rciE2uJcB29cgVwduIfcJl8dVjFtACS0q/ztva9CtuKRCVSbEoWUWH77NPd0SSDRc78q0EGpAEB3epCrvdF23bHNAAiddJn1NMMoJTJ4I9HwsTBDYBp0dxAz7c7FxtLXAC1TuyTEBD4QFOb8kiF8NKwdMVHQ4TCZCiFlACsXapuOy1+WjEOWcBWvZAmfWWwqg2XoEXHc7KD1ABG+DKg/amCn26N2YCOwZbaMEEHS4XY+TDo82vthK9/zzB5EwgeUlgASfA4uGMyTkLp0t2BidgAQbusd6BF/LdT2Da2+rBVF/B5E7ABEkQBXLbdhMQ5CVQ0RU9aIOm523QAxtQAbIFvQ3gBE7QAHRuVBCM188N3s7jtiz1TdfFBHG+HriV5RxggejN5+it5/jIARZQvbhF565B6XIO2ffGgT1yFjg4E0zwBE9w6DARBdvVABOQAQA2YRzAATpmARmQXrBVUU4ABSe+gSMnMyFEZvalO/pdH7B+4rAHaHe+Abq+6zr26wSmWg1A6cT+GwGouVbYOCVU5cNu6KceEtsFYbkFW7hlJNte7vkmNPbEOZHGPMEDzXJjYh5Yj1oy7P9PwOTy3WOwte4p6lwj++5Q0O1ctJb3NLiG2TaUsnpMkPBQEOuHDvBo/ivv/uoV/+8ZpOYidU04o7l2vCCVdDxKEQWFnvAWj/Ha8StwbugJb+itviL5q9xWqJw2P4whweQUDwXDDvSGPvT+Duszf+KBEzn4nt+ydEcXNb4lbxyF/gQUT/VCT/QdT/HmLhK0rjRjxVB8lPMmxWWgLRxwDusyT/ROAOstr0FKkAAHFU7BRjJ3xFkPgjCOLjbaNRJLbugWT/SxzvaxzuRcrzSGfz8a9SLTkjuqg/JAFPNo3/E0j+hlsiMwc++NfTqKEk2pbix5Aom58pzvvvaCv/YAb/j/sRNHW4wpVAEpMkVJp1Jfm4HmGU/qhh8XmRXEr8pVjGdXiUVsRUZsUN/1HV78LhMFt0LeC1XvEiMqtcJN/G4q/UISts9Fgvv1LjJd8oTfWqKo9raQjn9SPEHqdD4TCbAqli+H6D8e6RdFJgM41Av84wumJf/QMCrVfD1vW2U7lrtVAJHkgcAkBAcqUZJAycAGSZQ0HEiAIMKIBCUqIbBw0UaOHT1+BBlS5EiSJU2axGhQZUUlSSA2fOhwpUqJAxkWnJgko0CMCGvOjNjyQcudMBsg9CmUplCiSg8CdZnSaVSIBYcenZqxJsKZSU5+BRtW7FiPDqX+nGrTodqjMqWm/zz480FRtmYznnV48adRhEfZ9owZNylavS6fwpxZdWGSKD9VKoarEy/GBmQtX8YsNvDSvRMl7rTZIEqEB2qHAm5psClPrBAfJgUMlCvomYDvWjRNsOqDhjvlJoEgAQKEqkclPlaZVndm5s2db7xbWC3q33FdQrkw4YEE7rx1v3aJvC/SveNfR89r2CFM6d9fT+Y6feVCCREkPJiQYUQQQVFmXuzLopjwmus5Aw8MyzjziBIwo+LWQwgCKVSIYYsRLKBAIA26K40n38a7q6q7eqJpPght80mywZg6j0QHBdpOAg2Io+CCI7YAIYYYVJgiCvlCS25ErEb0CkEjjwRJwf/W3hsRqcjUimKKFnSkEgQzLqxggga4sw+CB7w8racme2otL/LSe+8v6p7USbUGShtORi+TqPEIF3KkkkoVqPCvJeMmOiupJV9DslBDG7gtt6COUhAp3aKsIk9JdfTAhREuqCBDgbaUccP7SiNgrgDV0gq2IRn8q9ShSvuSO09LU2ICCjLAYAQR8Jw0Tyt63G2iXkuF7S5DhzVSUDR/i4xRp5wYI1dnYwABBA+w2MKFEzDYIAMKJtByy+Ai0GBD+4QbjlVzWfUyTlchCDc4CRo4StYKLKjVhS2ygPZZZ1vwwgkfJWvzIDYZMlUJYg9+DjUUZ3tsxZai8CFSfSeW1IP/FqodgYMjsM0gg0wpAJlbbnESmVuQKaigggwsuACDI0ag1gN8caVYXw+06CIK5RwMUKlRDUI4aObcW9KvgHXzVYkow6C5ZmdB+ILiaHOkOgt88526aT0ldrpmIsLookfrBAb2T4JTkqgyodcmK2AUBSSRRdWi6CLqrp/9oosz7uabSjAA+IKIvnP1AIwwwvACCv/aIrhJrEhUVG22J//KM/Fsu0krmR6IgooupBg8TzC66EKM0O/2AuzPezgdBTC46CIMLcZgbLoVo9vsrbQp590k2ioCUi3Vfm5JCwDE0LpmFsTowgsvupjydIql6IILLZ4PYwwwiEh+UhBQsOIL/7DDsF6LHj8jE25gxfz5gd7fF8kis1J0VDH0jV4oCihw5gIMGLo+w+uaxwUukG8F0tNX3gi4wALGjgtfkIIYqmAFClKwCmKQwhW48LzmaYGAHuQceWATLKTlBiHwQ+FHEMUa8FylYTyh306igIfUNU8KVvCAs1hABCtIAXsMhB0XcohASZ0Bdh4E4gdVRzomhgEATZRdEs3XmIW9SFECkkxDUrjFjQwpaYQp0aDyRwAveFB1D4wgGMAghi98oYGxQyIQqyc4IupIBmBLYh6R6AUC8nGDefwgF5TmHtz5KScCe9xDuLjFRrEvPli0CZOkEiUkmpGJTyTd4bQQR0CCTYYKRpCe62BHPkCW0pRA9EKPIAe3X8WkbD1ZZAoFMyKeAShuyBpRFKwHxEqeMo/YG4MYrGCEM3ige5TiIRvHt0tfNlOKXPjNRU4FPKjYhACxRGFUcFfI15QpKCrSis7GwElnnlJ1iCPgFSD4BTFgsI1jeGMUyznPBW5ScbNZEFZUtJoPtUly2P/snWccybOkCKwnZ8uIzphJz1NuUguHOxwToRjFXjK0nF7g02Jyc6qiUQQo1wTo+x5Jy2CRiFFwA4xokjBOi9Jzjy2F6QenyKB+brSkAENLSN+nzduV9D2509xBfMTSmKLSeRBFalKVitRNFpWBWlCAzjQqnvBMp5DocZ9Oe3ef35WQaEGKzVAI4J+FulSpsxuDOiGYgx/kIAeJcGtcc3ADKbTxC2MY51L9SM9U+mcoKjqad06TRUG1T6u9u8Bw3iSTaP7HTIUNmH/6UMZmJnV2X8jBEGRQhDKMYAtm2EJot4AF0mbhXqQlrWhFm7EyFEEGOZACXh8KUXL+copSxZ3/F89kVSfdpTQayOph2XYGFbiAAsEJjKOatM+OjkooUYjSHwGZOvKpcwhF4ABoU2ta0YLWDN8Fb3jB+1nyiha1oc3YEHJw12VOd6avTAprlsI+B3EnCRXYggeEO1xjgsC4GwrKNiV5EzWFByk6mwJl5eiFL1iBA6Hl7mfFO2EKV7jC5U3tFsqQgwKScoFl7MNYcYsi+8WQhK2iwAhAoAIQwGC/QjvDG1pQTBaPYALADZH6BgRDFe0GMNB1gvX8mDoplIFaobVwkpW8ZPGO1rRFSF09tcAnKtLGxz4V8AM2VAEXQMsDMCjmGV6MsGK+wQPFhEGOjvAlwUKlLco6aHoI/8aYJExByF6QQRawwGQ+93nJ9yrDBkGsNBGOSS8DHaGWH8BlL8MABi0gAQxIMGZiEeHMlz4DCVpgzBhcQNGrQUxoesuVsLIGukqYAvmo5WdWt3rCMQhCF/qgOKmuqVG/8TGnknCBq1lMxpLW9BvETOlCYZoEYT5zmmOQhcQCN866Pc93StUmpHCuMVS4l6u1zep7qYHWDgNWjqnJEHZJYAIjyBOYPWBmGUf60sQ+0hnacOxL/1rTYM4Rs28MAZLK1zSoubJkoHvu1G7b4Bc2radHjCLczVcowK1Rl6l0ZjTTG9nFhLeRLl5vjmeaSke48bvGM7/CrGggTHACE5yEkP/7TOAIZij4wbWt2kslQQO3HmHaekae7QD3Aluo2BkeHemhS9rRkZ5xxg208TAfXdK/LiaVRkABAHeTTD+7jVZS7oRE6roCtRrtkSUsc/G6ALShXfWltESa9RGgVKApWKggfoSrVUnTFYe0pFug9zLrV+nOyXQLzMx0SAv+yzAYoo6mXp/TVEcyZ0NKA1AOhSboszT3aQDKbDSCs4/W86pFstnJ23nQn9dCI8BAdrTDoc0RAF4kDapBwrVroHvvDGEmOtIj7e43SFref2eOpYs573lvHNh6x3eeRlABLUMAi+gZTyIf4gTqM0ExrcI8nWrUslqNwPvgtZcIzPAGM5j//UreR33qMZWhN3En+wNZDxOY4HqHPXJLwK0Aup1F8XUX/t673zvk84A2AL7MwLQz2zTCQ7rBi7o8YTabuw/zyAjIm0CC0BkmgAIngAL5gwmNujwOIQ7vSIKRIcEJKIg3aQAwsQ/7YJWq8isCkD/r60ABexN2eQAKoLtn4T8ZG7zdKzrdQ7wwK0DLQIE2KL516z96O7q747gZ05ojqAACADD5aTwXIQ8fgRfqe4KUmz/hCR42A8NzAUPnIzCC0A0Y3Drr+yuxgg0tMzdaqb2n4b9i8sF7Q74gNLZhG8Kw8LUDzDQ/hDQS8MGnuzRnmbpPQ5uCaZFqcwnqg4JH5EJE/7mIgeiTURMYt3gul2gIeMHA6ps/s1gLyQgVGYmACbgAiZsY/sM0xHO0QHS6vHO0R3u3PQQLJNy4NkC2dju6vdM0Jry9xJOULbgAAgCXMLkqhxEIv5I8DHzEDNw6GISX14MXrmCUaIxG+du6J4BErlMUyBEO/LgA/ZMaRwszZEM+APw/R+u4M6PFk/DDM7O4M2O3L+PFH1zATdOXS1ECDWA7hsOylqAINNTAZhxIDaS+g3TGg0TIgXzELVRDOvOZCSxGCsCAOKyZOfTDV8w9VsTDGIPHFmhHkxhAEjhCpjs8o0tHvrPFBnyW5UtB4GqkY0yO2pG8JnCCJ9hChTRIhf/MQCjAyS3cQOsLlUpskZ6TgPu6Eb5pMXVjul7kxaeMRd97Rz0MyZA4gwScymBDwI30P8R7A3e7SmB0liwYgQwADgA7lSpSCYeIgms8SG28yZv8yYNsAg4ME7NgiC/hx3eJuNDBSJP8SpQcOt3Lu3esSpGwNGE7wHbrO7xLR6LTO3p7AxkTy2dxgSPIjgeIANJQkEISkDAhNGvkRN6wxqHwkUfijZ6jkXAcgbrrm8MzyUxDs3PMu8fcO9wrx8P8CA+oN8EjyTawRXiMSh/MO1hUxzKbzMqcGAvJzBnBPBCxHDakxFVxEtAEjcubEfz4utaso630Q5I8QI2MRSAURMP/uzjd9AjZDM6m9L+nLE8B3DgzmzHlpBjmzBAtc07qPMa4YQoYiRF+LI0JqIBwtEgiWkozG8/4DMBzjMwUQMn5jE+qPEyL0cqmbIPaNLqTFMwFFE7BGzz67JoruQBtEQhX2Uz3Q1HugIAoYJdxaQnNsxPXrKOJ+8XYXMzDi7QUqMNWBEtju1AzQ89FUEwzK8kkDESoHE8kXc/1xMVj6huMwYDUS5mTAZkBvQAo6L4RcAEZndFJsZgancpVhEzblDQH3T3c7Dj0HEB4DMtMM8J1G9PB/EE5dbpH+1A6VLcu9Zo+AJzo0VOb8UgOdVM2DU8M7UqjG7rCm8o30E0L7c3I/6zNeiQBM91FJuzBMtu7ZAPRLgUDPgWATwWAPhiCP82VLJgxlWS3wjPJXYxMSFVHqRxSSOu7w7TRXPwyyKxNHUVUDCWBML1TxCNVKikCGwDVYv1UH5CBYPUyj/RKQp1HG93VXhTMogvTM0CBqvTVemRVVoTMqLzVwmPKPEw25DsDJx0cI/BUY1VXIcCBP6U4O4xHHkTTIvXWB3VKlLxFeiPAdnRT4BzUxoRFd4tFXaXHbm1VHvRVedzUuymCdFXXhw3Vdu1ONMM0WDS8D/3R7zTOrnTFruzBwhu8dvzSbC1PO5xWlDTTwmzMasW0ciWiOoDYmP1UHsiX0xlZ9VzZO/9dR0yt1Eh9z0F8Rwb0uwLc2d+st42U1uKU1o18RZ2t1TdggdCRFmMiVplVVxuIgUsz1/3zyKZ0ukhDU5yF06/lWCDc2EvlTSLYw3n113GlzfFsVXhtz2YN23i9OJftGt68vb3xAB+wWmPdm3Lkzbzd20fNvfZUUH9lVac83JJ1Oo6TMX8tpqFVOkhr21UtzAz9wbL92lh0WnE1yZoBgcItRCP4W1Ad1VwEM3zUl9GVRZ1tt4Cl28U0PPFkXB4tulb8ypU9NpAEPpatOJMdTnDV3P8LQOAF3jOIWjlUTIyMgRw43RrI2vBct2Lqnh28uA1l1bDluHO0w/AU2Htb0uH/m1WlA1Pc89feRQGj41xJ01BuZd/cQ9+s5F7lfFfBK7O2jQFA+FtQyrTjrLfb69U8Gd0e/ditVFq9u9N4rDgeldZojUoiIDpxbdu/61Xci11kQwGhQ8lJfVBWxVFwveCb/VIGrtZiWt6sFeCVvbistVqs1dv+E1sEdFl5hNDFxNPDJURka9veq9dejF1uDcAJTlyLyzix7bs7FWDjJEzHNdhBBDbzHOF/rVYwY4HRDTOsvDiLi4FEkNm9sdPexDR2U8wktrgKRWDiJDopztjcrVThdGBIW4ThtFVky7hqZWChM16yhVTGhUpflGEjHT4TvrhYFcRazSEegNhRXVK03EW2dwXMS6vTdNxZJJzkTJWxwOvF/xMz4SNhTC0+YttgHzXPMebgHC3ZzK1U+I3fMw3Oz0XioBVUkizlvYmBqi1WHVBhQlXPy1VFREYz2ZVd9lxadfxcyFyEpQ3aWRyzLa5lja3Tb03SO3RVIv7OQQZlXk7YOsa0GDBdY01W5MVUoW3KprNXbQVkczxnycTQ4dyICY5hscXFMfPlxgy2Y7vK3hNYbxXYI01lNdZdeLzQj/xQpyVkbebeGBgCdaVZWBbXDz3jjDW+zu1K0NVQxsVUP460jXi00fUAFaj/1jEbyUfmTYQVQmp+4OE03jHV1kau5Fo9aAUlgRhQZGMFhKzVVxKI3IPO5Bud6D32wSQspgXt4/hMQkTdiHI9gYG4gDdgsZ0ePso9LA9AARaLYWNSAYsDSTlV2vYMtjlAAU0zghxogSIYAjAYgqjc4izeXYEWZ4vuu/19WGMy6nIeX7dWZ90DwuPz0C/D0VbV5tjd6I1wgXCRkQe4gBaQlvMkNkXIkm3hlgw4gcX2uyg+R9o1sxwoAkkbgiEgARnoARIwgiLoxW020iMs0nljzN4sSRd+2CLY5VxsgSItYkw1ZwblSFS91eE9x6GGW8j0Ow7gN4qYEQtgMSGEt1Zh/5VOmYAE5OhKjdPdO7MykIEb2Lu5+uwegAEjwKEtlmifrlaQDVpZzaEiWOQYiGUifeZBhd1CReVYhEVAXFp/7utgfuCNeAMIYB8tm4AVk9Axw7qH0IAMGF2Onm+nHOrA6wEZGAIUKIIeuAEYYPDXKuN4vbSSNGGovtVUtfAwiwEZgFiaPcAiJdKY7j963VBeFF+4PT7jtdV200VW5AgPGQ8NSAJGVbqo8BOfgIAJYMe/TuCxvbQFH23PjnDQhoEbQOO11mJS5vC6Bs8W/gGIvekB9E02rmVabmsWluTcJc9XPdTIXPLgVGuOoAAJkEAlkIC/i6ReMTfenOPDw9HeNP9HI+gBD7iBHCCB7QFtEnhwh6ZD9pxHQLfoGHBYwI0Bh9bZUp5tQsZtD9ZhFvdgPOzBSX5cPVQENBc3l1C6QwMeCOAAFXjuqORVY5NwI4CBISACCV9w7SYCMOhRNzVPKS7l3c1y9LXcJu/bmAUlPEbTHiT0Jm5Vf/ZyFu9Ir847teWIDiGbE8q4TSG1yFsEv7vKuCVeAKTYx/XeGYtXSGvvutbYgka2GCACmU3dnM5mYNbm355mpKVN8TXqGA/CjoiKqpKMZwdIByGY4FqETJtg+B488f5fN27lJoflmObpW/9wmf2BrF3v/lvgy9Xyd+TRrjRbroTiWKTdbi0LUln/jH96MXjBIojwiG01ZvAeTPesx+q1aNp+ay4HzueV2SrX2SMkdBZ+4lct0zu8XY0m70xrN+P1CKWwPJDfr6R5D5A/ZYuPzR7QbliUYKPrAUtDATs3gjWN5bqVeIlnOpqWWR/gTYTm5YlHZFY8VF718orm8r5DVKlmHKQxGGJTjqvwiPUt3vk8OtzrgSHYexSANCtQ8hZAgRzgoTPYLCMggnQX6vE+Qm7P16ir6ZgVHBv15XYzwjPmWXZP6ZSc769d7V/rbRUCmEgqkpAfkJKLe45AUFKf4oqlbg8wAhkQxBywAgkGbSS8fW6OTa1U769k2RzCZYjtde/20XX8brY//7yKnlMd7er3FPjeJM6PKBHKoLTTGBQtKvk+7lZ49QAiyIG+d7QhMAH/QYEbuPo3AG1shkcNB0zDS2deRu+/TVb1jF2XB3fci8oP7tlBHGGEBYg3Ht60IAEDBokzHhC2OEhiEcSISpQkIUDxQRKMETdy7OjxI8iQIjcqsVhyoskHHQs6hFHwJYkWAs/I7DHEphEPVoyQuGEQxZAcHmQkklHEg8KkA5EiJdGGqdKZJGJKfZqURAwjALZy7bo1RwyoYpWeSdi0jcyxSGG6jDmVpcGDMFkibEpWLcKDHRs0QFkyycSRggcTFoyxQcbEGAl0NBgTxtKyAgmSEAijh4yFOf96ypBxg0hDD0OIyOjRQm3UlwrbmC2rkOBk1UxbxBji9TaAPjHItmZK0KrvgS1YK3XsliHDxwsNLkzegvdM4XmR71XS16R164W3cx+MUcl3AoDFN+h4cPrBtZObXpYBgwgYEpvfxzc45IyMMlCdpi0LPPpdrzXlm1VY3YCbVzaEpRRw/kU2Vmyt0eVWQcc115ZcjkEWYHA0aejRRBP11Zd23Zl44kYEWJREX4plZB6F6Qn42ktE5NDZZT04pAZmRfTwBg5gdBYVah60QVyRBF1VkEIx9IGgV0TEwKRwSD7XmlltREdZQ3E95hhd6U0nnFsBeunQS3VVh5hJiaH4pon/fmUnXmDm5XUcQ28A6MFxcWGY4WnrXcUbWaf5159ZeyrkgQc+QNlVETFI1d+ADFIq4BsGsbQpVQuFOWGRSRka3HktdOTiYW7CuepgJ2V3EWIeocmcmXeih9BjuErFIY0FKtSbor0lFQMRj3YFllhbPpdssmhO5xiZLYlJoWsX9tbbeQ55UF1FFyVWHqvhgkQiiRYhViJH2U5IaVsNzWVhhhuedemDvAq7n1UxyGAsV7oBCOy8mXKY11wOUYgnhjGxB5OoUv0JwxkdlYTRYoChKy7GET2AGMWKXRzRtPIqe2ZzyzXUUkx3CYRktbyGKlYMOfC7lQ0gGHmvymP5+aWt/ykzhdxyLxPJZVzLgQiYx7FmvPQiFrM43nhKyBpXmDBs+XO2GR5XoUv/vhQsWgLr3KBdTs681Rm7Gbmfy2WN2tK7iF6V9bP0tvxzmB6xWLGrTC+9cUavnvRRvMqRle3BFXbZZXoR0hgby/X6Jlu1p8Vgw9kARPrbvSwDS9CsY87oweKJU7irWCijF3FHbXbMsd/invvdSSYRTvVU0ibusFua5k4XjYl2aPdZHe63W+YADBGWokIvRdlBKeyMssqdjj53f+9u6NF1f010WOzhBv70YiLerji1wUEf45c8i6wzkZGbGWAMRSR/x4KTs6ak/k6pfmdoFLKs4CHkejhbiv/VTOYn1nGke3NSVfjgVD7ruAhcdtqaoOzyoLwoEG4akpHzDlWVIsUseQrCl3Ai45QNak9aBUzWSzTYtgPKyCMdC894IggnV3FsIhV5kaxA2Ly5OQs5MWLIXeR3wJX5jHNIigEPkgeAtKnlDUtKja2cE6MqUgmLXlIK41wIsY9QRDw3BKIOTVQulOwNguny0wvLcp7UwYUlzdEQ12SSkFG5LWD7SQtsUrioGABCipHi0NWIFK/kQOZZcZScHNdyOqTMxFBsIcJHEuM9MyYhjSdqgEla9IAQdfJ8Qgzgy0A3qzAu5Slie40Amfg441mRKR6QovLyN6jJtQYhoAOTmOb/KEBC/dGXSYLLcrbnEU6e0YKe3I7FQhk1xhCOYF6iWqbOg8f1FO5h2UvWZHKGSJlkBZc/UJuDdtk83zGykTIiAWp8Nz9m0SRTLGFgAzepSZU8E5qjNAlAzXc+WpGuOKhcllQow77GCQd1bZMhwGqDyxM+FIsoq9qXfolIMnVJgF9sCjyz9hGOuWhF/dzOuXjoF2em61YEdZs9M8VFDSGMOUPEF9l4FYMf4HKKMeDPEAGGIU7V0XqprNcQZQIXGHwEh385jNROOhgCAO51igHJKnP1QmXdTSHO0SblEjWcLK3QZZEjZE+NoDbI3euXuoOJ4TboQmEd8C5vOQ9IXBXQ/49JFSRJAEzFOiYekNDFeF2j537i1cGXGq9hEOUQoxyFy+UhVoSRIWruEnsrSX6tKXzUbJ64ppdMQvWpaOxrSMaHHW+FBDl3ItLdfkk0rTqrrojN6ViI1VMAnJOYQzMY4+4KQC5BJpCIfINDljRJ1z7kIys642BRG5LAfuupIcHj6fzEtgftiTna/JNTsHQkoQF1hfraLSCYF8I7tsu7nd3Tv+4yl+ZlU7R+dWqI6iTdZY6yRcxkUUjOAMKKwlCbqjSivIYZqsqMFbZIKeFuqZiayP3yZMDcamKxpDKZJBKGXv3SuFgkopOMaL+Z/G9gqfkRAb/1puoUi+84JZcM+v8WkjB70m7VehVXotAyBmGB1jpbqAVfCksQ6xCexnXG15nYholZEXZO2xEB785a2nSZKvs0JrZOGIasGWsgL7fbXE4uNbTN2uQcyqeHujjDFsYnR8rXrR9qpMkcQVoz/xJgmiJKyF1MLAK1iDhcfU144kyhQHQ75hmgU4VhG8jWPlg05I5lQ2fiYFdDhb4xZlJOAJVyk6dZRheJRC4JBlaX4nkysHopTT67HvyS9Zr6jTk3kmpwQ5NpxMTBUjpxNF1HSfdRt4IJT3DO56t6WEo7Q6QBtIsynUotOk8l0nqaYmGMNaRrnHE7KvmyTU8BwSjJTerS06JSnrCmaUpWcS1HhuU0aaPGxjozGzHdswhV3RjEXBka1WCaiSP7tOpsFbRKZvmzR+/iAVpL0QcxkJTLVunaJBV42ANR1pUH4tWsJSS15hLRk1n/amJUQQ18IWGvkNsdIEuqm5Ggup7X9BTrciZv4bwZr1JUJ72dFXlu8PRQysU5KuTKK1shyS92sMNsiJDyuZoUOUdKxxSx/ppDZqHpoO+6XSy/TNEzU6ttJbM4FyLZzA0ZHeoy/hpsOZKp47q3SpcOVcFGDeob4RPi6plmnaEHKe0tmBj5aO0GhTdAaTvDzCJFvGqBFwZAftiA9/7KNkecLW4fqaf1unSSQtkvoIZRmsitM6V+yczJ2eKOhcelJbkS17MmgmQRRNlarqY3FnbtRRPs68qkMtgajVbdihYSBzodI8s2cbkCl2z9YjWLGqZ4zovm1QlNezV9nozCOkyW/7AUEjfn3LuHrGKZtviJLZpKJMK3C18YHoyRIrEq30bJ7JM8ecQlEcwcBxhPLwYvjG85osrREpsVxMPhWFfoRhY4WGxEBwAJnLxY3IcRmJmMDF2IBJ2hCnnM36vgm5zgn5esF6wVSqdkEcHElwxBVNiUFVM8XBRxhYLEwGHtkgHdXvtNB8PEkzCxx1y5xAluXHOllj5RBHio2H5tjOdNkNKIRIz8nr1Enzqti3PMSNgFIFmkDYQ53Fr1IFQwV5oUF+WkzlzdINHMxS4F13mwwEgsWXYAWKiBx7dgoGCAAAsAmVG1jHYNStDJVZ+AYB1uncKcQRaYzeGRlw9q2R3V4f/5QcVnzQ30LURMeQALPByxjEQQhlJUId+oWVUZCYYREAEMrAAogmBl6SCCHcSGiVXkpCLZ0B6j6NgJUkb/4R6/IRQV8gkTks6RyaBYeAAorsB7YEYO9MFIeAz9jdIl7lcbeY8bOtvxfQQg7AAezMCN9AAJ9KIvYtOCDYwdhcySwNciaiGHLMhGRYXvGIT0nB6ilKCwAFIXTQbBsAcvgiILnAFmDIEOzMEO1EAN4IEOCGNe0YklipidjRLJuY5I4AE/CoEQIIENIAEP3EgnskAvMoraSUfFnVnkrZ9/iBWHyM+CKYlZlGLfSWHK+R4tcZRAWKMHoIARBMEN6IAQ2ED/DUCjDugAP+KBPzrXSpFcGwKkJuHbSNxkTeIBD8CkPiIBHtwAGPhISspjcqkQmlTS//2J3IBjY1mlWdVLHkVa1SQLVZggh6ikCViBS86BEOxAQwpBTQ6lUNrk0QmOPtndM8lb8nWMSPSBTQ6lTfKjXupjDaglDwyBj6CARIZiAFbYlonihpGN5yCJR/7KdxWbFo3jzyxFPIbiGxABDshADvzAHNiAD/hAQ/JAUQolX94kHohEvpkLqsilJy3Zk1lMUOblaeblHKxlTdZAF4SmDejADQyBDBgBCsCTNRomPPnYIgUV4bFGgfDYjvmZZ1GFsLQXdS4VXCjcZU7kGRBB/xEUwRD8AA/MgV8igVEiwQ4gZV7eo16mpwWuFieVBBH2FSiVEX0GDgG4JkSkJ1/eZnqm5yD850zi41HOAQ/8plHgQCcqhDXO4RwSFOf035Ec3KsZ3KGtn/59GCN518EwSmFO5C+WgRV0xhDcwAzMARIMKH+uJT7uAIuqZU0SqGm6pUiQS0n5EPKRHAUJVEjEqE2G516qpxD85V/ipk2a5YnWwIkiwW3eQA4IphX0AAocBAuAgCQ+XBaM238YCYfVogzS1dqlYMIwaIdOpEwQQQ+EaBB8J2mep18iqRDcJl/q51qeJYuS5z36qJyOxHzm6H+NnJwxE+zcpXoW6Z2maP9NBimi/ihRIiQPxOk9LuSRziQ/SuMQAGcRGEGClsXCBWKVVmkgjhuohiqosgCoxgCVdqokroAcPh4RmKkRFIEMpGlnHmqkIsGb9udatiWBzkFb4oF5suiupid/IqSeyolgUYSJPRsb+RC9gQRCvqgOhKe08uqh/iUguKhe3iaeImRb4qZZAgIg6CO4AkIf9AFp/sAPNGmTGkV3YmoPtCoKxKtrnMEZtMEZvEEbQIy9JkW8tiqmvqoVwKoMVCqT3kCj3iObHiUS2KqhDmWj1uaz/uidqidfsuh57gBp7uq26kAaihiUucgxShVg0Gh/UZBgoOaLTuvBwuS1Dik/aiz/HsBonMYoj7IlTvaBEIxrDYwrz5JrueKluRLlDPAAeA7t0JLmwd7Bz/ZBz4rrTNaAIOBjzOKqig4qjMIobUKrivLAHdTmPf6qksIsauZkXpGI/WWidFXQvMnmbN6kxl7BHRTqTIKr12osgd6j1+YtzXLrwx4s0B7szS5tuQ4C05brDpSrEJQrHwguX8Zt3BJprj6sbSpqyhKoj+pqePLt3Q5rTVqskoYn3HJtrlJi7azUMkqXf4XIavWFYNhmxurAHYhu5+ZskG6txk5r1d4mnGYt70ZrxNIsbS5qowatXj4rQtaBuSZvUQJt8Qpro2Kt875stO4qzKqnyk5rsPJj/3jW6efGrczipGAElNOZC+ouX+nylUfgpU3GLoHeQex670zmY65Wbuh+r7TKadai7GlCbP5K7qIaL++ipv8Cbv7qpY/urvPyqrSqLPXywBXA7h2ELgN3rsWq5fuyb3gKBsmllLk4m1StEQWVD1+07sseMNdqK53uACBkq7Q6btxegeVmL8XK6cyuZw3zKA7r56JKbA4nMPTup8q6rwPb7QI7LtfGbqGmZ3iC7eZy7U1q8MdSzAaGSBLqEAfqVX7hZ0Qw6t2GLvta7A5gq1C27wWXKBEHK+Uqaq8Cr/42bwDrMA0XLxDbbcqqLAT76BVg7xFfsA7U77Z6rt3m8R0YBv/IftrrfE8zxg4V12igjoTdGvGu/uoK/2iwtrDj3m0ES6v0zq/XvrEn5/D+4i8Ot+XjPjADH3HowvD71qT7TiwGC7EQiy0P0OnCkrETC8Z8dovrzFnHXFUEidiyuiFUnazGwu4C/2oYr+cEt/Cd3sEMuC8G6y60hnLeurHe8q8NWzMn82Mr34HdfkEr3zH7sjIGwy3sJvEdF7NNMrElDwbI1s5P1p2+Mc0/8dCckVQid8Qc6K4Jm6jF1iYaz8EMwDDXPjAEVzLnirIc8zBbpnE25y/KqvGgunK0RjAEw/IFPy5/Ou4zx65BkzEr5/E+RysYI4FIc6xheAvcMWv9kRL/P8VONI3YGU0MGzprH78vaSKzWgLwncLtHUwBOF8wM9MxfxY1/gpr75qm8bLxQ+Ovts7B+96m45LzEXOtj+KpVLtwKQu1EE+r5zrzHBDGT6ouiZkWVJUYTJPUsfLyXxmf/H0ENBcqE1euJccuHrgwtJ7xylZzxHJuryq0QvN13YZnDFt1LBvzU3vzQLfvR1c1HzezR1suHpT0IA8Gm9Sfe4LcRfDQYDBtz4Jrx/INinXLd5xLPkNEKxflwlqsw6Jx3OIpLBOoQfsxHVtt1e7neho1Us8w5yJwiuo2Uc6BT6csLBfqFTyzODtzN5MzVzd3JFssYTibGyIyVP2Xf/ny/0Z49mdv97hOV7fICX1y0miDRHh6MyAf7K4u9gkXZftiMgSfcyZvrhtT6+ROrq7Od7bmNm4nMBIjcVHbMTR3s1Zr7X9b7R43alHWaWpqsGh3HhYHTg9RRBRoN3d/tgrnLM+Oi+lmx7PFc/mEhGzH7w7Y7kWzMlTf70bzsXLzswIn9O/25ybrtqH6djbvt/aeuDc78GH7tOyu8nvzpxdrbf2ycsrCJBIUhsV0DBY/+HSbRBRMgSBUOBgXLs9iOGhzT4123i5/uGD8JbA+b8Y6tkCb8n9j9BHrNTr/9jTH7Q3nNozv9rDOMUjDd1E+dvsaOGR3dB+37xdMAWQP8QEj+f8/vSH8KcZll08UUEGUqzC5XqujW3mVbzf3fAfJHTKdoK+zzmSu7vNVp3iOB/k5h/pWn/Kwsvn8TrSMu/lud/LtDjkZC3dV6/aQ33SJZ3TXwjZOhzWSRwGdRYGvU4Ra/5AQLlmiLzqjb/cg8CzOIi6LdncD6XL9zZl7mgjGxmxRFjRx43Q4pzp8X7BIh7maq2fXDuV/v3icD+qLT22hKvcra/v7NvZhv/efC7Exx3esFwbTToGv+3oSMMEUQIEU+5Aldt4PRQEUCAIYMzqG/yxOQm5eOvtGMKOSq1R1vwmhzrnGpna81+8VALULx3oxP3Vwr2cCa22covEM03WA43H/Rjv2OKczVcdyVJd3rGdwSFA4zyL8FFDBFEwBIHiBEPD6+dalYuw7Eyy64Dp8adYs03JLFNdo7Vh8H4v5QCdxNwtyNzfqx8MymZ8ynIM57k7zD++3XkM17D5z+x4xzHf6Wmo0ns47TnfEZD/juB77ZwsC3uM9IAjCFByhJu07v6sIFEABz+NlxEbrXnJr4lMuX5Jtsx1yELrK/cFJXJMxvfO4+3a0y8f69K54eAZ1A29ucGfs7bY4e5s8uUurOdfkca+8NIs6gcc+VrP+OHsvRFxswue+7id7z/I94PN6FIgIEww+z08Bt47BFeBBHTwst/I0ALcxX+7FBaohCGvx/2BYNEhD8+lr/7ZXtTl3s+XXex5rcu3bewRnvFMXeXPHNTT3eWObfSZbdEiHdEG7PNzevu7nv8WCa86qMEDsAARIoKApSphAoUJlSkMeePrwGHNlDB6LPOo8tIhHhw6OHz1aDOmRJEiLfRalTPkgCUslBJK8jAlTyUubBJSo1LmTZ0+Vd+50vMMjqA6gPOYIncNDx9KkTYcefdoUacelQIPOuWJUB1KiUomG1cqVqlOvSa9ejcoVqNCqPK7cmdGWrty6RqNiVYkEyQ6/fwEHBjyQoN8+fYQcxqNxosWKHzE+DLmxpEmTlUeK/LiTAM6Wn1mGbgAatE/Tp1POQfuV6P9Wqk2tMlUrW3bXpF6PAp079Mps3EPn5P16xSse3ktfF11d1DjV3FiHOg/6/CtQnX0FZx8M6HAfiCQ7dt24OCTTyeNLYv64PjN7zSRRqgydhCZMlzFZ1k/SAHV/n6uTwqoqHeKCSzmilorLKgKBs82q6YQLsCwH8SLKqLPsUu6KKb4AriqzYMPrKLxie+o563TSLrs+dviOo/C6Ou899CgDKbP0ZsQRpKQsC0mnzkjLT4kGhkwiyJz8S5Kn4C68MLjdsrKNqbbU2g0up4RrK8Qqe6NNOg+1vOoh6Ii7zaw7FLQwN9cO1IsnFXfwTiQYOxqvRvV6nFGz9XpECzaO/ARa9E+O4kuJSCX2+6wmnGoiUj8klYxUJTyCQzOvqFrLykKyoFvrreBYK/CpSpVz0isFjRr1wqCI2m1CvGZgsijd7nCKwTt8UvHF8Cyz0T08cbzxMkGJ3fFPknjE/0ynBkabDydGD302tCElrfYnAetiDcIvpujyudhem63bAckyM7Yww0KzRAGvck2tAwPUEkXTtOPVvWFzHLa9ffe899hkjQ1Yh0IXITI/0qKtydCZ+LPW4UVq5TQv6RaTqqu2ULWVqg4bJEvBBE/8UESvhAKT5FI/TXUO/7Kr0989deQX32DfSxbgQWHjUdCbl0WUUfoQdZbagg992GikSOW2TLGYtpXK1s6lMmorqYvKtYuhllVBqTVGsypclRQMYH3JfrnYPAW2Gedi1+Zz2fkSTnQ+o+nuieM7OIrS1qS2TpetBuXtaOunw3RORBEBlxpVAhG3trC/JpN5pDn0Vf877cn/RRYzAM8SmVgdhFDJpiBJY7Tu03mC0KitgGJd76/cgg03LKFMbsB3lT4Xtun+RrythwNbambLNQ80c5HUvtnmzp2+4wu0nDfLeIvkm0lRmhqwb78HUO8+tcXinbgo1m8PD8QvxZqwwFln/VBkp7lCq+6B/jJ2+oB35EGIGjT/XPl/kdKhOQgwgJ3yCFac0qEb6WRIizoUkfjDKER5r3vNq05dCOcut/QmaqmaAZs29a6zCMVbrosLUL7QvcIgQQg0K17OiseDGuSgCDZIj612VhbmdQpLQMnb7soCFOMRzFFIOtTQHEXBClLqfSNk1d9KFRcOdQxV0BmZmZj/x5aR8W5e8wPMzkYovRg6xQYriMEM+JdAH+pQjZTbGhTjlzP3aYxPeDiNTZglHyVWUHBn2orT/BQd9oWnVrATH7nm8EHpQU0ql5Ja9/DwFyQA6kPRQ4olk2VJHxQhBitgAQ9scMmISS96WBEKDAF0rI+g0Ck5JNRpSLNHJVIqjvGCTVxUQqoTWshEX7oKVQZnsWBOSIwc8d7jFnORHu6ukJSDig5s8INOdpIEO0DClMpyNwzyjpJqZOPXmlkVYqGGAKORpRIldCYwBcUnCISQuo6iwcPRRUS5/NoJnydOO3ZPkvf0EzONks9R2YAEMTCoQWHAl3VFCYZgJOUoofI8/zm2UpXntKhpNgKcEzZlo/tMUqUOyC4nrew0E3onDo/pFyFQknfJw4utbGCEgx50BSiwpkf2pko2ElBjDy2LgliXmYsOdSeqSZW2uLIZohb1N09zpkdPJ0lmivNGnLNBDqY50056YA7XpCoOWSlKIUaPjVFqjuqMt9SlIu9r6jSmWlXSFI7F7ywdSqlfwIe0AppVh0iYwwrMqFWD1tQGixxgW4wjxNuJUq7hFCPvynISuF40lUHp0lOhqlbfCZSx3pNk3gRqSvh1yQZBEKxWV1BDNC1zeXuDXbwee1nPmWSyFt2IqNCqkdou4oewJeZdW4S4JjqNB349rWBXEAQbWP+RawV0yht7+7HqfNOvJNmtLCVkym0pdbI5jJdE34q6FZoIkxiSaK1sQITjnjYHheWBOB8Kv5xOB5y4uexVc7CDgV13jy2ka/Pwltml3jCIiPXsXwKp2MNacQ41kEFg16vVIdRANXVtZoXSuUMPBbIrfHmwDGpAPf5S0CLLuWyIBEzUEu8wqSl+WCRVShJNkUpCOqjBDCAcYQnXILQXno5sg8Mxb60WQzbeQQ/MGAT+uXjED+sDssA5VxFP1iN7lR53xRtjYsm3I0JAggd0vN72OqlEXzuqLSH0Wo7VgAdgNqgMbMjkJlvLmfDDimZ228PvCs8jFPQLC8tMvDnYgJP/YT4tYO/Av8uyEsNISaxTt3nVrMYAByHWwZwhyVYOB2XKcH2VnmHjZ5Uij2PMK640DX3cFZCgBtdspGi/adjZSVqrRlgyplG3ZyfiubbGkahrhSdna0k1fK1r5aBRkOoIv4EvgGPj6lY33y4hoQamFWwPgovr08kJgWEM4G4Pt+Bsgk2F9TPzL5cCSmsrW9Uo6CoxeTrd1q0zlOo9LQqE0EKCaZvOMsbLifMGbkGJ9pJPpuDjnjLwQt4BCTpgt45X4IFmn9fHXKwlKHNgxhwflASH2S+/nQxGp2JZrZ+bsTgPjuCqIiUuNjjDw8OMAkBH6cKPjc6ghzBpwbIADyu9/zTIHaazAxazz70uHiZJXjfAkDefRymtzmF+Whws91VeA3aqnh5m0EEE6A7zTnn2psBOl1yV3eZRyv2is24z3OFRN/QQqP5cgoOIL0bY+HFnoF9hd90nmkYhdJJOVALPOPBGg7Ffzo20GiTb7YZur539iZTCEuHux83BrfkuqRaumFRx3PseNf0n6SmxMEKQDI+GQujKN/60cG+qpoBjgyEAVtk3wHzmlfSUMp0ywD6qbc7Ki8KxR/UvprbBDVbP+taHkknQFuImO5l8wYK46LhP0texwrGbfX6WMvYhE0GqxC+CX/JuVn6q21sbAVGbk9I/LZyrb/3+tPCdxPR9d//HaGbuR6qf7cI41M8vwn7Ahr4GlISgB9yuCJZs3+Sv75CHRIppt/yH5cxK/MwtQPyK9gIw1STumq6CzTzA/dbLCmrgyfYP955K9BxtPcBtkeip8IxmvEompkRwAwcrBs6ALyQPq2rwuMrA0hiwAXni6wCmgEpCAjnvjXSG9BDMK2zgwWzw4c5gB2wACQqN9YgAEKxLCE+Dc1jr/uAqrwqHtkTNmoLsmnowCm/wDIRAps4PBhLj47jQJ+SEUniqonoNUO4msuIPdb4IdJDg5dTw4dIwzODQO4JwDlPjN3CoMiTQd/hw+JTuz/xLCApqEDHR0FgAdORQEXdCTnbnyrakkMr+iUcU6OzQbgdaaA52gPEy8RVVTX+4zhOXxNQoaiPybITyJmJg8MX+wr9qAAFhcRgF6wcAYRZpUSfkpI1ERbd+zyLwBoaOZY8K4xhtDAeIMRsP6vI6MRkX4aG4iNe6S9bGZo+kCpquUBuHccKQ0RsXYaXmSrsiS+B4aq78hBrrx8aKoBDV0e2UrBuTMUDkq3NOsHteSqzwsAyt0QbAoB+JUcn/2tEbsU+NmqlDChJ1djGnugkfY6wGcs4hYREMauAOElER64yxlukiT2eixEn4VLI/qrEjkOAGQBIWEyHESnIOTZCYdPEl6WZH7LGzSI8gAKGFAIEmaxITVyDf+jAZM4qsGK0Xz0nhAIQ5OLIoQYcH+DEpDU0BX8kdU2Lzwg3WfNLwRmLGOCa8vIdFYqyFNJArA1ABTRAsJ2XgtsQRjc6wTEkSiW8HlswS4bLxVgAGUAAHiuDy/CsndfJyyBD/wK+K/kSW6Ee/8g0GAlMTYaAHrEAGhuAHQAcQaiA0XYYuc4ltLKcsH4aUFgRgzikfg/EyB4sFYAAGiKAHiiAIbuAG/0AnNG0gNBNjJ6VSEe+EIkECCUtNasQRHzvCwWpyMInACIoADG5gBiAi32qgN2ugKJ+MV3SENIuqm8ZkjXDx96DDeJbQooKrBpASFmWTCKwgCIYgBx4CNHsTNFcKFIVFJFaKL0mTCAXoLoMT9JLKFpuy+/oAEC5xAz0ABWwzPm+g50LzOmvgPukkZjiihULHO/1DJJBTlVDTYVCplL4gOWWJJNTT7QazMA9TPnXAL7FzQreTTkDCBHuuxDTUYcRyVEztQ60lf0jlkYbqI2rACsJMNjWTMz3zQCM0O30OPODDTjA0Q2/0dDQjrIKMcvjTtrpJi6KRR/uDJPZHBnoABv88IDOhMzpzYAYGhjdDs0VotDLsZGDqZErPKUcPsvmy9Jwm531GYq06og9C0zuEADQllElj9EX0ZPNIik5LzrsuySgCtPustCfVSiwHJg5fhNPgA0zBkFGvSywdalAeEbb2ahQFr0bY48k8ruc8FegoI5OcpzE9zaGEaDKeUSS+TkpbNfO+zkefxkslpWYMJ1l2tVj5KLFCa1CANVIcagWP0Fih1WiI8E4JUuBCwrBCLVq1tVrUxrJaZzyQ0LIuSaA6dVvN9TSE1eJMVbMqlCzeqyPONV5Rwzy16DwnSzVUo1bwdV8pRzHlVVsnU0WEwC9qoLYehy/6AmER1poEAhD//lVeDzRgA6Mo/eJxHFatLHZQB3Zjs4MwLvZhjZUwBmEQBlWlivJkAWEQVNFiMfZkB3UgBuFxTFYIRjZmR9ZfQVYia3ZkU5Y7erZndxZmSfZjLypla3Yg+CBmD3RkaXZnnXYgcpZOhdZpbXYQkpZqrdZoY5aoppYPetZreRZrn5Y7otY7tVZsjxZsY1ZteZZoz+lstfZs0XZsyxYsp3Zuw9Zr2fZol0pu8fZv3bZuudBv8RZsgXZnC3apauBvGZdvBVcRCXduI3dks7M/CEEGCAEOLjdzN1dzMfdzTaMObGByG/doA/dxca90GdcGhEARDkEREAERZAB2FYEQFKF2/2EXEXDXdjN3d3FXd3l3dhVBBg7hEEBJdfH2dFGX70hXdbOTEA4Bc3OXEGK3en2Xd683e4EXEagXEQ6BEES3eUt3eYVQfAEXEGTvEKrXete3fYE3d333d7dXd+nXew9hAG0AeakWaslX/sx3bke3DxQBB9y3gN3Xd2M3e23XgL93CPrABvJXf2M2cftX/iR4gkNpCIrXgDnYgLF3gQ/4g2v3dR0YfSO4cQO4gsu3dE2YzTT4EDRXfjuYg3N3htv3d78XBxLhBx4Yfe/2aCGYO+BAheeQcAdCQkeXB37ghWv3fW24g2Xgidf3erkXBwiBEIaAKQ4UOwVhdPP3MBKBiFmTUWRTlg/ea4ldt3ixV4rZuI0T2HZr2HutWBGGoI5/4I7hIIzF2FN793bj2I0B+YmbuHrVQA0UAQ6GeI/LtncLuZEL+XYduZEVIZIpWZL9+JIP+YoV2WECAgA7'''
dats1='''R0lGODlhfgAsAHAAACH5BAEAABkALAAAAAB+ACwAhJGRfYeHdIeHdQAAAGVlUqurm62tnaurnKysm2FhT19fTaCgkrKyoGBgTqKilKWllmNjUKenmYqKd4+PfIiIdbOzoa+vnaqqmaiolwAAAAAAAAAAAAAAAAAAAAAAAAAAAAX/YAZQQGmeKEpmbOu+cCzPLUHQuHzteTymwKApBrEZjYrbLHlUxghMpDPTrMZ2BsNFS8NuLyyScDxaUCixaBU6qypka6MrLn9ttdltN88VlXoxYkR0Nm9PVodrhiyEUxkLO3d3M5J5LEOAL5gvUQqeao6MRkU2g6OFpTVIEBAKrHaRBgs9eHhgfgCZmn8wpKlUTTCgdXOjNEc4WAaAypKXvLrPucLIqsTWN0gw1W3XMF99OQta41/S0S2bLr5TwS/a3Ng48d9bsz3gtbfquvwsasV+YbsRZRu9d97sWOoxThaffdCi+cvALmCogsC8AewmEAYfFpEoZXmUpc/EHhM7/8Ux+EubRTZw6LSwlUFLJB4vGs4aV+4cDDQygE5ktybRooOgICQqCrJSyYUusIB86tMFCaAvAtxLSUcpSwJeM2BEeGTRQHckwanFyUJn25IQp7UQE9GE0IgtiDJtMTZjx39NzPpFlEHZuLfmWiQuDK5qBrp2H59wzJfbRnkBBedtEnYw2nEORs5cfOdeWpPQKJghM21ovCidG/09a5FSaRd8ljHWMzW0bkwlIAuhDPgaWtmzaYtKThJqTWeGdyxoeAHSBeCssctdFw/tsJUcWyZUjMd04Y9ebOqLpD07cbHduSGHKQM25hi1zOt7VOmOQ5vtsfZeRZURc5BfNFx24P9oorHw0Xlb+ObbU9fxkp12ach3hFdlLcVIEmS1Mx6DtzyHBw0L+BYXOgPKVuBsAG3oCVqeodVffrrpkEVo76GEV3F0HDVihy6eRWM5ucmCQ0OiCXehCqbEYdaCCBIiWCMv5GZPDv7F9WQKK1CjSIia3QcKiCHu1QJPWZg3A5sljuBkdmGyaOedeOap55589unnn4AGKuighBZq6KGIJurnBRXUw2hUIV3Blg4VVFAipJEqyqelMFRaqQueNhqDpzOESuoLpmraJ6eoWioqC66+GpWrl4L6aam1qqonq7Y+2kKsVzTK66y5olqsrncOC6uwtzB6aqsZ3AotDsoii2eBtZ+yyqm0oILh67Q0WJqptXZi26iv28oKUrbcLrtsu9GGSu61ubILq7t2sFuvqPIaO++u+77Lr7rxpgpuvJ0e+28m5sK6w8AJ30Sws78SXO3CujRcWKW3tMuxYh7zCu/FGAOisbMQz+ovLJGM3G/JDAeML8K2Hgyyp/s+C/POMIcAADs='''

imagePath = PhotoImage(data=dats)
widgetf = Label(top,  image=imagePath,  bg="#3399ff")
widgetf.place(x=40, y=0)

imagePath1 = PhotoImage(data=dats1)
widgetf1 = Label(top,  image=imagePath1,  bg="#3399ff")
widgetf1.place(x=310, y=27)

select1 = tkinter.Button(top,  text ='Select GIF image' ,  command = select , height = 2,  width = 20, bg="#ed4d3e")
select1.place(x = 300,  y = 100)

convert2 = tkinter.Button(top,  text ='Copy Base64' ,  command = copytoclipboard , height = 2,  width = 20, bg="#ed4d3e")
convert2.place(x = 300,  y = 160)
convert2.config(state='disabled')

reset1 = tkinter.Button(top,  text ='Reset' ,  command = reset , height = 2,  width = 7, bg="#ed4d3e")
reset1.place(x = 320,  y = 220)

close1 = tkinter.Button(top,  text ='Quit' ,  command = quit1 , height = 2,  width = 7, bg="#ed4d3e")
close1.place(x = 389,  y = 220)


top.configure(background="#3399ff")
top.resizable(False,  False)
top.geometry("480x350")
top.update()
top.mainloop()
