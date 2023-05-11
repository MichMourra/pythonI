'''
NAME
    contar_nucleotidos_v2.0.py
  
VERSION
    2.0  05/05/2023


AUTHOR
    Diego Carmona Campos

DESCRIPTION
    El programa cuenta los nucleótidos (A, T, C, G) de un archivo con
    una secuencia de DNA.

CATEGORY
   Sequence    

USAGE

    % python contar_nucleotidos_v2.0.py

    El programa recibirá:
      
      a) La ruta al archivo

      b) El nombre del archivo
    
ARGUMENTS

    path: La ruta a la ubicación del archivo con la secuencia de DNA.

    name: El nombre del archivo con la secuencia de DNA. 

SEE ALSO
'''
# Imports
import argparse 
import re 

# Functions
def count_ATCG(dna_sequence):
    '''
    Cuenta los nucleótidos A, T, C y G de una secuencia de DNA.

    Args:
        dna_sequence: El string con la secuencia de DNA
    '''

    bases = ['A', 'T', 'C', 'G']
    for base in bases:
        print(f'La secuencia tiene {dna_sequence.count(base)} {base}\'s')

# Main
# Definir errores
class AmbiguousBaseError(Exception):
    pass

# Iniciar el parseador 
description = 'El programa cuenta los nucleótidos (As, Ts, Cs y Gs)\nde una secuencia de DNA proveniente de un archivo.'
parser = argparse.ArgumentParser(description=description)
parser.add_argument('path',
                    type=str,
                    help='La ruta a la ubicación del archivo con la secuencia de DNA.')
parser.add_argument('name',
                    type=str,
                    help='El nombre del archivo con la secuencia de DNA')

# Parsear argumentos
args = parser.parse_args()

# Abrir archivo
try:
    file = open(args.path + args.name)
    dna_sequence = file.read().rstrip('\n').upper()
    dna_sequence = dna_sequence.split('\n')
    dna_sequence = ''.join(dna_sequence)
    file.close()

    if len(dna_sequence) == 0:
        raise ValueError()
    
    if len(re.findall(r'[^ATCG]', dna_sequence)):
        raise AmbiguousBaseError()

except IOError:
    print('La ruta o el archivo ingresado no existe') 
except ValueError:
    print('El archivo está vacío')
except AmbiguousBaseError:
    print('El archivo contiene bases ambigüas.')
else:
    count_ATCG(dna_sequence)