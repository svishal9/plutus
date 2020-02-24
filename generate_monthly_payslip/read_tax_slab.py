import csv
import os

def ValidateEachTaxSlab(eachTaxSlabRow):
    assert isinstance(int(eachTaxSlabRow[0]), int) and isinstance(int(eachTaxSlabRow[1]), int) and isinstance(int(eachTaxSlabRow[2]), int), 'All data in Tax Slab file should be int apart from header row'
    return True

def ValidateTaxSlabWithoutMaximumIncome(entireTaxSlabWithoutMaximumIncome):
    expectedOutput = [[0, 20000, 0], [20000, 40000, 10], [40000, 80000, 20], [80000, 180000, 30]]
    assert entireTaxSlabWithoutMaximumIncome == expectedOutput, 'Tax Slab does not match with expected output.'
    return True

def ValidateTaxSlabMaximumIncome(maxSlabAnnualIncome, maxSlabTaxRate):
    assert maxSlabAnnualIncome == 180000 and maxSlabTaxRate == 40, 'Maximum tax slab does not match with expected output'
    return True

def ValidateEntireTaxSlab(validTaxSlabWithoutMaximumIncome, validTaxSlabMaximumIncome):
    assert validTaxSlabWithoutMaximumIncome and validTaxSlabMaximumIncome, 'Tax slab data is not valid'

def GetCsvFilenameFromConfigFile():
    configFileWithLocation = "../setup_config"
    with open(configFileWithLocation, "r") as configFile:
        return configFile.readline().split('=')[1]

def ReadTaxFile():
    inputStaticTaxSlabFile = os.getcwd() + '/generate_monthly_payslip/static_input/tax_slab.csv'
    tax_slab_rate_list = []
    maxSlabAnnualIncome = 0
    maxSlabTaxRate = 0
    validTaxSlabWithoutMaximumIncome = False
    validTaxSlabMaximumIncome = False

    try:
        with open(inputStaticTaxSlabFile) as csvfile:
            csv_file = csv.reader(csvfile)
            header = next(csv_file)
            taxSlab = csv_file
            for taxSlabRow in taxSlab:
                if taxSlabRow[1] == '-1':
                    maxSlabAnnualIncome = int(taxSlabRow[0])
                    maxSlabTaxRate = int(taxSlabRow[2])
                else:
                    ValidateEachTaxSlab(taxSlabRow)
                    tax_slab_list = [int(taxSlabRow[0]), int(taxSlabRow[1]), int(taxSlabRow[2])]
                    tax_slab_rate_list.append(tax_slab_list)
    except Exception as exception:
        print("File not accessible")
        print(format(exception))

    validTaxSlabWithoutMaximumIncome = ValidateTaxSlabWithoutMaximumIncome(tax_slab_rate_list)
    validTaxSlabMaximumIncome = ValidateTaxSlabMaximumIncome(maxSlabAnnualIncome, maxSlabTaxRate)
    ValidateEntireTaxSlab(validTaxSlabWithoutMaximumIncome, validTaxSlabMaximumIncome)

    return maxSlabAnnualIncome, maxSlabTaxRate, tax_slab_rate_list

if __name__ == '__main__':
    ReadTaxFile()
