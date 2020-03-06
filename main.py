from wolframclient.language import wl
from wolframclient.evaluation import WolframLanguageSession

session = WolframLanguageSession()
session.evaluate(wl.StringReverse('abc'))  # StringReverse["abc"]
session.evaluate(wl.MinMax([1, 5, -3, 9])  # MinMax[{1, 5, -3, 9}]
