import os

import utils


# def get_number_of_packages():
#     number_of_packages = 0
#     slice_index = 0
#     folders = os.listdir(utils.PACKAGES_PATH)
#
#     for slice_index in range(len(folders)):
#         if folders[slice_index] == "slice" + str(slice_index):
#             number_of_packages += 1
#
#     return number_of_packages


# def get_package_sizes():
#     package_sizes_per_slice = []
#     number_of_packages = get_number_of_packages()
#
#     for slice_index in range(number_of_packages):
#         package_path = utils.PACKAGES_PATH + "/slice" + str(slice_index) + "/package.zip"
#         package_size = os.path.getsize(package_path)
#         package_size_per_slice += [package_size]
#
#     return package_sizes_per_slice

def get_package_size():
    package_size = os.path.getsize(utils.PACKAGE_PATH)
    return package_size
