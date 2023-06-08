driving = input('你有沒有開過車? ')
if driving != '有' and driving != '沒有':
    print('請輸入 有/沒有')
    raise SystemExit

age = input('請輸入年齡: ')
age = int(age)

if driving == '有':
    if age >= 18:
        print('通過測驗')
    else:
        print('你不能開車')
elif driving == '沒有':
    if age >= 18:
        print('你可以去考駕照了')
    else:
        print('再過幾年你就可以去考駕照了')
else:
    print('請輸入 有/沒有')
