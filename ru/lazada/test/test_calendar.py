from unittest import TestCase
from ru.lazada.main.Calendar import Calendar
import pytest


class TestCalendar(TestCase):
  def test_check_year(self):
      #Check what year > 0
      assert Calendar.get_year() > 0, "Year should be greater than zero"

  def test_check_month_and_day(self):
      #Check what short month [4,6,9,11] must have day in 1 to 30 and long_month[1,3,5,7,8,10,12] must have day in 1 to 31
      #Check leap year
      #Check on febr month
      month_short = [4,6,9,11]
      day_short = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
      month_long = [1,3,5,7,8,10,12]
      day_long = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
      day_febr_leap = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
      day_febr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
      assert (Calendar.get_month() in month_short and Calendar.get_day() in day_short)\
             or (Calendar.get_month() in month_long and Calendar.get_day() in day_long) \
             or (Calendar.get_month() == 2 and ((Calendar.get_year() % 4 == 0 and Calendar.get_year() % 100 <> 0)
        or Calendar.get_year() % 400 == 0)
        and (Calendar.get_day() in day_febr_leap)) or (((Calendar.get_year() % 4 <> 0) or Calendar.get_year() % 100 ==0) and Calendar.get_day() in day_febr and Calendar.get_month() == 2)  ,"Invalid date"







