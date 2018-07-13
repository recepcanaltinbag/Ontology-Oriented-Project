from OntologyQueryFunctionsDescriptions import *

#Some Useful Functions
#All of them returns Lists

WishedPollutants = GetMyWantedPollutantOnly('Fuel Additive',None,None)  # Send(Types,Domains,Effects) returns
print(WishedPollutants)                                                     #Pollutants (Micro+Metal)

Types = GetPollutantTypes(LoadOntologyForMe())
TypePrinting = PrintingNicely(Types)    # To see Types
print(PrintingNicely(Types))

Domains = GetPollutantDomains(LoadOntologyForMe())                           #To see Domains
DomainPrinting = PrintingNicely(Domains)
print(PrintingNicely(Domains))

Effects = GetPollutantEffects(LoadOntologyForMe())                           #To see Effects
EffectPrinting = PrintingNicely(Effects)
print(PrintingNicely(Effects))

MicroPollutants = GetMicroPollutants(LoadOntologyForMe())                    #To see MicroPollutants
print(PrintingNicely(MicroPollutants))

MetalPollutants = GetMetalPollutants(LoadOntologyForMe())                    #To see MicroPollutants
print(PrintingNicely(MetalPollutants))

ConvPollutants = GetConventionalPollutants(LoadOntologyForMe())               #To see ConvetionalPollutants
print(PrintingNicely(ConvPollutants))
