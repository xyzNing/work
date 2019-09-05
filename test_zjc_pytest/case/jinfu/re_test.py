import  re
re_email=re.compile(r'(\w+)@(\w+)(.com)$')
# print(re_email.match('someone@gmail.com'))
def is_valid_email(addr):
    re_email = re.compile(r'[\w\.]+@\w+\.com$')
    if re_email.match(addr):
        return True
    else:
        return False
print(is_valid_email('bill.gates@microsoft.com'))
print(is_valid_email('someone@gmail.com'))
print(is_valid_email('bob#example.com'))
print(is_valid_email('mr-bob@example.com'))
print('ok')
def name_of_email(addr):
    return re.match(r'.*?([\w\s]+)', addr).group(1)
print(name_of_email('<Tom Paris> tom@voyager.org') )
print(name_of_email('tom@voyager.org'))

print('ok')
print(re.match(r'.*?([\w\s]+)','<Tom Paris> tom@voyager.org' ).group(0))
print(re.match(r'.*?([\w\s]+)','tom@voyager.org').group(1))
