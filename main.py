import vpackage.validator_script
import vpackage.validator_sort

if __name__ == '__main__':
    print('nice')
    validator = vpackage.validator_script.Validator()

    validator.load('82.txt')
    valid = validator.validate()
    vpackage.validator_sort.write('valid.txt', valid)

    sorted_valid = vpackage.validator_sort.quick_sort(valid)
    vpackage.validator_sort.write('sorted_valid.txt', sorted_valid)
