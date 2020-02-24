try:
    from read_tax_slab import ReadTaxFile as ReadTaxFile
except ModuleNotFoundError:
    from .read_tax_slab import ReadTaxFile as ReadTaxFile



def GetAnnualTax( annualIncome ):

    annualTaxPayable = []
    maxTaxSlabIncome,maxTaxSlabRate, taxSlabRanges = ReadTaxFile()
    for taxSlab in taxSlabRanges:
        if all([annualIncome > taxSlab[0], annualIncome > taxSlab[1]]):
            annualTaxPayable.append((taxSlab[1] - taxSlab[0]) * taxSlab[2] / 100)
        elif all([annualIncome > taxSlab[0], annualIncome <= taxSlab[1]]):
            annualTaxPayable.append((annualIncome - taxSlab[0]) * taxSlab[2] / 100)
    if annualIncome > maxTaxSlabIncome:
        annualTaxPayable.append((annualIncome - maxTaxSlabIncome) * maxTaxSlabRate / 100)
    return int(sum(annualTaxPayable))
