from wolframclient.language import wl
from wolframclient.evaluation import WolframLanguageSession

session = WolframLanguageSession
print(wl.StringReverse('abc'))
# print(session.evaluate(wl.StringReverse('abc')))
print(wl.Now)
