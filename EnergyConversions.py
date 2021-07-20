compatible_units = ('eV', 'nm', 'wavenumber', 'hartree', 'kcal/mol', 'kJ/mol', 'au')

def convert2eV(energy, units):
    if units == 'eV':
        return energy
    if units == 'nm' :
        return ((1/float(energy))*1240)
    if units == 'wavenumber':
        return float(energy)/8065.6
    if units == 'hartree':
        return float(energy)/3.6749E-2
    if units == 'kcal/mol':
        return float(energy)/23.061
    if units == 'kJ/mol':
        return float(energy)/96.485

def convert2nm(energy, units):
    if units == 'eV':
        return (1240/float(energy))
    if units == 'nm':
        return energy
    if units == 'wavenumber':
        return (10000000/float(energy))
    if units == 'hartree':
        return 1240/(float(energy)/3.6749E-2)
    if units == 'kcal/mol':
        return 1240/(float(energy)/23.061)
    if units == 'kJ/mol':
        return 1240/(float(energy)/96.485)

def convert2wavenumber(energy, units):
    if units == 'eV':
        return float(energy)*8065.6
    if units == 'nm':
        return (1/float(energy)*10000000)
    if units == 'wavenumber':
        return energy
    if units == 'hartree':
        return float(energy)/4.5563E-6
    if units == 'kcal/mol':
        return float(energy)/2.8591E-3
    if units == 'kJ/mol':
        return float(energy)/1.1963E-2

def convert2hartree(energy, units):
    if units == 'eV':
        return float(energy)/27.212
    if units == 'nm':
        return ((1/float(energy))*1240)/27.212
    if units == 'wavenumber':
        return float(energy)/2.1947E5
    if units == 'hartree':
        return float(energy)
    if units == 'kcal/mol':
        return float(energy)/627.51
    if units == 'kJ/mol':
        return float(energy)/2625.50

def convert2kcal(energy,units):
    if units == 'eV':
        return float(energy)/4.3363E-2
    if units == 'nm':
        return ((1/float(energy))*1240)/4.3363E-2
    if units == 'wavenumber':
        return float(energy)/349.75
    if units == 'hartree':
        return float(energy)/1.5936E-3
    if units == 'kcal/mol':
        return float(energy)
    if units == 'kJ/mol':
        return float(energy)/4.1840

def convert2joule(energy, units):
    if units == 'eV':
        return float(energy)/1.0364E-2
    if units == 'nm':
        return ((1/float(energy))*1240)/1.0364E-2
    if units == 'wavenumber':
        return float(energy)/83.593
    if units == 'hartree':
        return float(energy)/3.8088E-4
    if units == 'kcal/mol':
        return float(energy)/0.23901
    if units == 'kJ/mol':
        return float(energy)

def main():
    print(f'Compatible units: {compatible_units}')
    units = input('Units of value you want to convert: ')
    #check that unit input is in compatible units
    if units in compatible_units:
        energy = input(f'Energy in {units} to convert: ')
    #Convert to  hartree, kcal, um, Thz, ps
        print('-'*50)
        convert2eV(energy, units)
        convert2nm(energy, units)
        convert2wavenumber(energy, units)
        convert2hartree(energy, units)
        convert2kcal(energy,units)
        convert2joule(energy,units)
        print('-'*50)
    else:
        print(f'Did not enter a compatible unit or with the correct syntax{compatible_units}')

if __name__ == '__main__':
    main()