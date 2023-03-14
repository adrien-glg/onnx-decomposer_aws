import package_size_calculator
import size_helper

package_size = package_size_calculator.get_package_size()
pretty_package_size = size_helper.get_pretty_size(package_size)

print("PACKAGE SIZE:")
print(pretty_package_size)
print("(" + str(package_size) + " bytes)")
