import datetime

def main():
  name = input('Your name: ')
  print('Date of birth')
  year = input('Year: ')
  month = input('Month: ')
  day = input('Day: ')

  birth = datetime.datetime(int(year), int(month), int(day))
  now = datetime.datetime.today()

  age = now - birth

  print('======================================')
  print('{} is {} years old.'.format(name, int(age.days / 365)))
  print('{} days after your birth.'.format(age.days))
  print('{} seconds after your birth'.format(int(age.total_seconds())))
  print('')
  print('Have a nice day!')

if __name__ == '__main__':
  main()