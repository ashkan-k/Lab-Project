PERMISSIONS = []

USERS_PERMISSIONS = {
    'title': 'دسترسی کاربران',
    'permissions': [
        {'name': 'لیست کاربران', 'code': 'user_list', 'description': 'دسترسی لیست کاربران'},
        {'name': 'افزودن کاربر', 'code': 'user_create', 'description': 'دسترسی ساخت کاربر جدید'},
        {'name': 'ویرایش کاربر', 'code': 'user_edit', 'description': 'دسترسی ویرایش کاربران'},
        {'name': 'حذف کاربر', 'code': 'user_delete', 'description': 'دسترسی حذف کاربران'},
        {'name': 'تغییر رمز عبور کاربر', 'code': 'user_change_password',
         'description': 'دسترسی تغییر رمز عبور کاربران'},
    ]
}
PERMISSIONS.append(USERS_PERMISSIONS)

######################################################################

ROLES_PERMISSIONS = {
    'title': 'دسترسی نقش ها',
    'permissions': [
        {'name': 'لیست نقش ها', 'code': 'role_list', 'description': 'دسترسی لیست نقش ها'},
        {'name': 'افزودن نقش', 'code': 'role_create', 'description': 'دسترسی ساخت نقش جدید'},
        {'name': 'ویرایش نقش', 'code': 'role_edit', 'description': 'دسترسی ویرایش نقش ها'},
        {'name': 'حذف نقش', 'code': 'role_delete', 'description': 'دسترسی حذف نقش ها'},
    ]
}
PERMISSIONS.append(ROLES_PERMISSIONS)

######################################################################

APPOINTMENT_PERMISSIONS = {
    'title': 'دسترسی نوبت دهی',
    'permissions': [
        {'name': 'لیست نوبت دهی', 'code': 'appointment_list', 'description': 'دسترسی لیست نوبت دهی'},
        {'name': 'افزودن نوبت دهی', 'code': 'appointment_create',
         'description': 'دسترسی ساخت نوبت دهی جدید'},
        {'name': 'ویرایش نوبت دهی', 'code': 'appointment_edit', 'description': 'دسترسی ویرایش نوبت دهی'},
        {'name': 'حذف نوبت دهی', 'code': 'appointment_delete', 'description': 'دسترسی حذف نوبت دهی'},
    ]
}
PERMISSIONS.append(APPOINTMENT_PERMISSIONS)

######################################################################

DOCTORS_PERMISSIONS = {
    'title': 'دسترسی پزشکان',
    'permissions': [
        {'name': 'لیست پزشکان', 'code': 'doctors_list', 'description': 'دسترسی لیست پزشکان'},
        {'name': 'افزودن پزشکان', 'code': 'doctors_create',
         'description': 'دسترسی ساخت پزشکان جدید'},
        {'name': 'ویرایش پزشکان', 'code': 'doctors_edit', 'description': 'دسترسی ویرایش پزشکان'},
        {'name': 'حذف پزشکان', 'code': 'doctors_delete', 'description': 'دسترسی حذف پزشکان'},
    ]
}
PERMISSIONS.append(DOCTORS_PERMISSIONS)

######################################################################

TESTS_PERMISSIONS = {
    'title': 'دسترسی آزمایش ها',
    'permissions': [
        {'name': 'لیست آزمایش ها', 'code': 'tests_list', 'description': 'دسترسی لیست آزمایش ها'},
        {'name': 'افزودن آزمایش ها', 'code': 'tests_create',
         'description': 'دسترسی ساخت آزمایش ها جدید'},
        {'name': 'ویرایش آزمایش ها', 'code': 'tests_edit', 'description': 'دسترسی ویرایش آزمایش ها'},
        {'name': 'حذف آزمایش ها', 'code': 'tests_delete', 'description': 'دسترسی حذف آزمایش ها'},
    ]
}
PERMISSIONS.append(TESTS_PERMISSIONS)

######################################################################

INSURANCES_PERMISSIONS = {
    'title': 'دسترسی بیمه ها',
    'permissions': [
        {'name': 'لیست بیمه ها', 'code': 'insurances_list', 'description': 'دسترسی لیست بیمه ها'},
        {'name': 'افزودن بیمه ها', 'code': 'insurances_create',
         'description': 'دسترسی ساخت بیمه ها جدید'},
        {'name': 'ویرایش بیمه ها', 'code': 'insurances_edit', 'description': 'دسترسی ویرایش بیمه ها'},
        {'name': 'حذف بیمه ها', 'code': 'insurances_delete', 'description': 'دسترسی حذف بیمه ها'},
    ]
}
PERMISSIONS.append(INSURANCES_PERMISSIONS)

######################################################################

RECEPTIONS_PERMISSIONS = {
    'title': 'دسترسی پذیرش ها',
    'permissions': [
        {'name': 'لیست پذیرش ها', 'code': 'receptions_list', 'description': 'دسترسی لیست پذیرش ها'},
        {'name': 'افزودن پذیرش ها', 'code': 'receptions_create',
         'description': 'دسترسی ساخت پذیرش ها جدید'},
        {'name': 'ویرایش پذیرش ها', 'code': 'receptions_edit', 'description': 'دسترسی ویرایش پذیرش ها'},
        {'name': 'حذف پذیرش ها', 'code': 'receptions_delete', 'description': 'دسترسی حذف پذیرش ها'},
    ]
}
PERMISSIONS.append(RECEPTIONS_PERMISSIONS)

######################################################################

WAREHOUSES_PERMISSIONS = {
    'title': 'دسترسی انبار ها',
    'permissions': [
        {'name': 'لیست انبار ها', 'code': 'warehouses_list', 'description': 'دسترسی لیست انبار ها'},
        {'name': 'افزودن انبار ها', 'code': 'warehouses_create',
         'description': 'دسترسی ساخت انبار ها جدید'},
        {'name': 'ویرایش انبار ها', 'code': 'warehouses_edit', 'description': 'دسترسی ویرایش انبار ها'},
        {'name': 'حذف انبار ها', 'code': 'warehouses_delete', 'description': 'دسترسی حذف انبار ها'},
    ]
}
PERMISSIONS.append(WAREHOUSES_PERMISSIONS)

######################################################################

TEST_RESULT_PERMISSIONS = {
    'title': 'دسترسی جواب آزمایش',
    'permissions': [
        {'name': 'لیست جواب آزمایش', 'code': 'test_result_list', 'description': 'دسترسی لیست جواب آزمایش'},
        {'name': 'افزودن جواب آزمایش', 'code': 'test_result_create',
         'description': 'دسترسی ساخت جواب آزمایش جدید'},
        {'name': 'ویرایش جواب آزمایش', 'code': 'test_result_edit', 'description': 'دسترسی ویرایش جواب آزمایش'},
        {'name': 'حذف جواب آزمایش', 'code': 'test_result_delete', 'description': 'دسترسی حذف جواب آزمایش'},
    ]
}
PERMISSIONS.append(TEST_RESULT_PERMISSIONS)

######################################################################

PAYMENTS_PERMISSIONS = {
    'title': 'دسترسی تراکنش ها',
    'permissions': [
        {'name': 'لیست تراکنش ها', 'code': 'payments_list', 'description': 'دسترسی لیست تراکنش ها'},
    ]
}
PERMISSIONS.append(PAYMENTS_PERMISSIONS)


class ROLE_CODES:
    LAB_ADMIN = "lab_admin"
    STAFF = "staff"
    DOCTOR = "doctor"
