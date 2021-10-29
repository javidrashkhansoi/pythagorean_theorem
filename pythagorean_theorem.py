from math import sqrt as square
from math import pow as exponentiation

from numpy import arange


class PythagoreanTheoremClass:
    """
    This class calculates the perimeter, the area of a right triangle. And also can find sides unknown to us.
    Even if you only know one side, this class can compute the likely sides. And at the same time, it can even
    calculate the probable perimeters and areas. You can find the perimeter and area of a right triangle without
    finding other sides.

    This class works conveniently and correctly using the "pythagorean_theorem_function" function.
    """

    def __init__(self, *,
                 first_leg: int | float | None = None,
                 second_leg: int | float | None = None,
                 hypotenuse: int | float | None = None):
        """
        Constructor of class "PythagoreanTheoremClass". At least one argument must be specified for the class to work.
        :param first_leg: Accepts only integers and real numbers. When using the "pythagorean_theorem_function"
        function, it does not accept values greater than 100. This is necessary for faster class work.
        :param second_leg: Accepts only integers and real numbers. When using the "pythagorean_theorem_function"
        function, it does not accept values greater than 100. This is necessary for faster class work.
        :param hypotenuse: Accepts only integers and real numbers. When using the "pythagorean_theorem_function"
        function, it does not accept values greater than 100. This is necessary for faster class work.
        """
        self.first_leg: int | float | None = first_leg \
            if first_leg is not None \
            and first_leg >= 0.01 \
            else None
        self.second_leg: int | float | None = second_leg \
            if second_leg is not None \
            and second_leg >= 0.01 \
            else None
        self.hypotenuse: int | float | None = hypotenuse \
            if hypotenuse is not None \
            and hypotenuse >= 0.01 \
            else None
        if self.first_leg is None \
                and self.second_leg is None \
                and self.hypotenuse is None:
            raise ValueError('No side length is specified')
        if self.first_leg is not None \
                and self.second_leg is not None \
                and self.hypotenuse is not None:
            if self.first_leg == self.second_leg == self.hypotenuse:
                raise ValueError('All parties are equal to each other')
            if self.first_leg + self.second_leg <= self.hypotenuse \
                    or self.first_leg + self.hypotenuse <= self.second_leg \
                    or self.second_leg + self.hypotenuse <= self.first_leg:
                raise ValueError('The sum of the two sides must be strictly greater than the remainder.')
            if self.hypotenuse != square(exponentiation(self.first_leg, 2) + exponentiation(self.second_leg, 2)):
                raise ValueError('This is not right-angled triangle')
        if self.first_leg is not None \
                and self.hypotenuse is not None:
            if self.first_leg > self.hypotenuse:
                raise ValueError('The leg cannot be larger than the hypotenuse. The first leg larger than the'
                                 'hypotenuse')
            if self.first_leg == self.hypotenuse:
                raise ValueError('The side cannot be equal to the hypotenuse. The first leg equal to the hypotenuse')
        if self.second_leg is not None \
                and self.hypotenuse is not None:
            if self.second_leg > self.hypotenuse:
                raise ValueError('The leg cannot be larger than the hypotenuse. The second leg larger than the'
                                 'hypotenuse')
            if self.second_leg == self.hypotenuse:
                raise ValueError('The side cannot be equal to the hypotenuse. The second leg equal to the hypotenuse')

    def hypotenuse_calculation_method(self, rounding: bool = True) -> int | float:
        """
        This method finds the hypotenuse. For the method to work, you need to set both legs.
        :param rounding: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When "False",
        numbers are not rounded.
        :return: Returns the length of the hypotenuse as an integer or real number.
        """
        self.hypotenuse = square(exponentiation(self.first_leg, 2) + exponentiation(self.second_leg, 2))
        return (round(self.hypotenuse, 2)
                if rounding
                else self.hypotenuse) \
            if self.hypotenuse - int(self.hypotenuse) != 0 \
            else int(self.hypotenuse)

    def leg_calculation_method(self, rounding: bool = True) -> int | float:
        """
        The method finds one of the legs. For the method to work, you need to indicate the leg and hypotenuse known
        to us.
        :param rounding: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When "False",
        numbers are not rounded.
        :return: Returns the length of the unknown leg as an integer or real number.
        """
        leg: int | float | None = None
        if self.first_leg is None:
            leg = self.first_leg = square(exponentiation(self.hypotenuse, 2) - exponentiation(self.second_leg, 2))
        elif self.second_leg is None:
            leg = self.second_leg = square(exponentiation(self.hypotenuse, 2) - exponentiation(self.first_leg, 2))
        return (round(leg, 2)
                if rounding
                else leg) \
            if leg - int(leg) != 0 \
            else int(leg)

    def perimeter_calculation_method(self,
                                     rounding: bool = True,
                                     limitation: bool = True,
                                     only_integers: bool = False) -> int | float | list:
        """
        This method calculates the perimeter of a right triangle. For an accurate calculation, you need to specify
        the length of at least two sides. When specifying the length of one side, the method returns the likely
        perimeters as a list.
        :param rounding: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When "False",
        numbers are not rounded.
        :param  limitation: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When
        "False", there is no limit.
        :param only_integers: Flag. Optional. By default, "False". Accepts only a "True" or a "False". When "True", step
        becomes 1.
        :return: Returns the exact perimeter as an integer or real number when specifying the length of at least two
        sides. Returns the likely perimeters computation as a list when specifying the length of one side.
        """
        probable_perimeter: list = []
        if self.first_leg is None \
                and self.second_leg is None:
            legs: list = self.probable_legs_calculation_method(only_integers)
            for first_leg, second_leg in legs:
                perimeter: int | float = first_leg + second_leg + self.hypotenuse
                probable_perimeter.append((round(perimeter, 2)
                                           if rounding else
                                           perimeter)
                                          if perimeter - int(perimeter) != 0
                                          else int(perimeter))
            return probable_perimeter
        elif self.hypotenuse is None \
                and (self.first_leg is None
                     or self.second_leg is None):
            leg_and_hypotenuse: list = self.probable_hypotenuse_and_leg_calculation_method(limitation,
                                                                                           only_integers)
            for hypotenuse, leg in leg_and_hypotenuse:
                if self.first_leg is None:
                    perimeter: int | float = leg + self.second_leg + hypotenuse
                    probable_perimeter.append((round(perimeter, 2)
                                               if rounding
                                               else perimeter)
                                              if perimeter - int(perimeter) != 0
                                              else int(perimeter))
                elif self.second_leg is None:
                    perimeter: int | float = self.first_leg + leg + hypotenuse
                    probable_perimeter.append((round(perimeter, 2)
                                               if rounding
                                               else perimeter)
                                              if perimeter - int(perimeter) != 0
                                              else int(perimeter))
            return probable_perimeter
        if self.first_leg is None \
                or self.second_leg is None:
            self.leg_calculation_method()
        elif self.hypotenuse is None:
            self.hypotenuse_calculation_method()
        perimeter: int | float = self.first_leg + self.second_leg + self.hypotenuse
        return (round(perimeter, 2)
                if rounding
                else perimeter) \
            if perimeter - int(perimeter) != 0 \
            else int(perimeter)

    def area_calculation_method(self,
                                rounding: bool = True,
                                limitation: bool = True,
                                only_integers: bool = False) -> int | float | list:
        """
        This method calculates the area of a right triangle. For an accurate calculation, you need to specify
        the length of at least two sides. When specifying the length of one side, the method returns the likely
        areas as a list.
        :param rounding: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When "False",
        numbers are not rounded.
        :param  limitation: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When
        "False", there is no limit.
        :param only_integers: Flag. Optional. By default, "False". Accepts only a "True" or a "False". When "True", step
        becomes 1.
        :return: Returns the exact area as an integer or real number when specifying the length of at least two
        sides. Returns the likely areas computation as a list when specifying the length of one side.
        """
        probable_area: list = []
        if self.first_leg is None \
                and self.second_leg is None:
            legs: list = self.probable_legs_calculation_method(only_integers)
            for first_leg, second_leg in legs:
                area: int | float = (first_leg * second_leg) / 2
                probable_area.append((round(area, 2)
                                      if rounding
                                      else area)
                                     if area - int(area) != 0
                                     else int(area))
            return probable_area
        elif self.hypotenuse is None \
                and (self.first_leg is None
                     or self.second_leg is None):
            leg_and_hypotenuse: list = self.probable_hypotenuse_and_leg_calculation_method(limitation,
                                                                                           only_integers)
            for hypotenuse, leg in leg_and_hypotenuse:
                if self.first_leg is None:
                    area: int | float = (leg * self.second_leg) / 2
                    probable_area.append((round(area, 2)
                                          if rounding
                                          else area)
                                         if area - int(area) != 0
                                         else int(area))
                elif self.second_leg is None:
                    area: int | float = (self.first_leg * leg) / 2
                    probable_area.append((round(area, 2)
                                          if rounding
                                          else area)
                                         if area - int(area) != 0
                                         else int(area))
            return probable_area
        if self.first_leg is None \
                or self.second_leg is None:
            self.leg_calculation_method()
        elif self.hypotenuse is None:
            self.hypotenuse_calculation_method()
        area: int | float = (self.first_leg * self.second_leg) / 2
        return (round(area, 2)
                if rounding
                else area) \
            if area - int(area) != 0 \
            else int(area)

    def probable_legs_calculation_method(self,
                                         rounding: bool = True,
                                         only_integers: bool = False) -> list:
        """
        This method finds the likely legs by specifying only the hypotenuse. When using the
        "pythagorean_theorem_function" function, the length of the hypotenuse does not exceed 100. For comfortable and
        fast operation of the method, it is recommended to specify the length no more than 100. The method returns the
        length of the legs in the form of a list containing tuples with integers or real numbers.
        :param rounding: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When "False",
        numbers are not rounded.
        :param only_integers: Flag. Optional. By default, "False". Accepts only a "True" or a "False". When "True", step
        becomes 1.
        :return: Returns the probable lengths of the legs, if only the hypotenuse is specified, as a list containing
        tuples with integers or real numbers.
        """
        probable_legs: list = []
        if self.first_leg is None \
                and self.second_leg is None:
            for first_leg in arange(0, self.hypotenuse, 0.01
                                    if only_integers is False
                                    else 1):
                for second_leg in arange(0, self.hypotenuse, 0.01
                                         if only_integers is False
                                         else 1):
                    examination: bool = self.is_it_a_right_triangle_method(first_leg,
                                                                           second_leg,
                                                                           self.hypotenuse)
                    if examination:
                        probable_legs.append(((round(first_leg, 2)
                                               if rounding
                                               else first_leg)
                                              if first_leg - int(first_leg) != 0
                                              else int(first_leg),
                                              (round(second_leg, 2)
                                               if rounding
                                               else second_leg)
                                              if second_leg - int(second_leg) != 0
                                              else int(second_leg)))
            return probable_legs

    def probable_hypotenuse_and_leg_calculation_method(self,
                                                       rounding: bool = True,
                                                       limitation: bool = True,
                                                       only_integers: bool = False) -> list:
        """
        This method finds the probable lengths of one leg and the hypotenuse by specifying the length of only one leg.
        When using the "pythagorean_theorem_function" function, the value cannot be greater than 100. For comfortable
        and fast work of the method, it is recommended not to use a length greater than 100. The method returns the
        probable lengths of the sides in the form of a list containing tuples with integers or real numbers, where the
        first number is a hypotenuse, and the second is a non-luminous leg.
        :param rounding: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When "False",
        numbers are not rounded.
        :param  limitation: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When
        "False", there is no limit.
        :param only_integers: Flag. Optional. By default, "False". Accepts only a "True" or a "False". When "True", step
        becomes 1.
        :return: Returns the probable lengths of the hypotenuse and unknown leg as a list containing tuples with
        integers or real numbers, where the first number is the hypotenuse and the second is leg.
        """
        if limitation is False:
            limit_of_the_other_leg: int = int(input('Maximum length of the other leg: '))
            limit_of_the_hypotenuse: int = int(input('Maximum length of the hypotenuse: '))
            print('\n')
        probable_hypotenuse_and_leg: list = []
        if self.first_leg is None \
                and self.hypotenuse is None:
            for hypotenuse in arange(0, 100
                                     if limitation
                                     else limit_of_the_hypotenuse,
                                     0.01
                                     if only_integers is False
                                     else 1):
                for first_leg in arange(0, 100
                                        if limitation
                                        else limit_of_the_other_leg,
                                        0.01
                                        if only_integers is False
                                        else 1):
                    examination: bool = self.is_it_a_right_triangle_method(first_leg,
                                                                           self.second_leg,
                                                                           hypotenuse)
                    if examination:
                        probable_hypotenuse_and_leg.append(((round(hypotenuse, 2)
                                                             if rounding
                                                             else hypotenuse)
                                                            if hypotenuse - int(hypotenuse) != 0
                                                            else int(hypotenuse),
                                                            (round(first_leg, 2)
                                                             if rounding
                                                             else first_leg)
                                                            if first_leg - int(first_leg) != 0
                                                            else int(first_leg)))
            return probable_hypotenuse_and_leg
        elif self.second_leg is None \
                and self.hypotenuse is None:
            for hypotenuse in arange(0, 100
                                     if limitation is True
                                     else limit_of_the_hypotenuse,
                                     0.01
                                     if only_integers is False
                                     else 1):
                for second_leg in arange(0, 100
                                         if limitation is True
                                         else limit_of_the_other_leg,
                                         0.01
                                         if only_integers is False
                                         else 1):
                    examination: bool = self.is_it_a_right_triangle_method(self.first_leg,
                                                                           second_leg,
                                                                           hypotenuse)
                    if examination:
                        probable_hypotenuse_and_leg.append(((round(hypotenuse, 2)
                                                             if rounding
                                                             else hypotenuse)
                                                            if hypotenuse - int(hypotenuse) != 0
                                                            else int(hypotenuse),
                                                            (round(second_leg, 2)
                                                             if rounding
                                                             else hypotenuse)
                                                            if second_leg - int(second_leg) != 0
                                                            else int(second_leg)))
            return probable_hypotenuse_and_leg

    @staticmethod
    def is_it_a_right_triangle_method(first_leg: int | float,
                                      second_leg: int | float,
                                      hypotenuse: int | float) -> bool:
        """
        This method checks if the object is a triangle and if it really is rectangular. The method is class independent.
        :param first_leg: First leg. Required to indicate. Accepts only integers or real numbers.
        :param second_leg: Second leg. Required to indicate. Accepts only integers or real numbers.
        :param hypotenuse: Hypotenuse. Required to indicate. Accepts only integers or real numbers.
        :return: Returns true or false. If the triangle is rectangular, then it is true, and if not, then it is false.
        """
        if hypotenuse == square(exponentiation(first_leg, 2) + exponentiation(second_leg, 2)) \
                and first_leg + second_leg > hypotenuse > 0 \
                and first_leg + hypotenuse > second_leg > 0 \
                and second_leg + hypotenuse > first_leg > 0 \
                and hypotenuse > first_leg \
                and hypotenuse > second_leg:
            return True
        else:
            return False


def pythagorean_theorem_function(*, first_leg: int | float | None = None,
                                 second_leg: int | float | None = None,
                                 hypotenuse: int | float | None = None,
                                 unit: str = '',
                                 sides: bool = True,
                                 perimeter: bool = False,
                                 area: bool = False,
                                 rounding: bool = True,
                                 probable: bool = False,
                                 explanation: bool = False,
                                 limitation: bool = True,
                                 only_integers: bool = False):
    """
    This function is auxiliary for working with the "PythagoreanTheoremClass" class. It is very easy to use. You just
    have to specify the parameters you need.
    :param first_leg: The first leg of a right-angled triangle. Optional. By default, "None". Accepts only integers or
    real numbers.
    :param second_leg: The second leg of a right-angled triangle. Optional. By default, "None". Accepts only integers
    or real numbers.
    :param hypotenuse: The hypotenuse of a right-angled triangle. Optional. By default, "None". Accepts only integers
    or real numbers.
    :param unit: Measurement value. Optional. By default, "". Accepts only a string.
    :param sides: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When "False", neither side is
    evaluated.
    :param perimeter: Flag. Optional. By default, "False". Accepts only a "True" or a "False". When "True", the
    perimeter is calculated.
    :param area: Flag. Optional. By default, "False". Accepts only a "True" or a "False". When "True", the area is
    calculated.
    :param rounding: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When "False", numbers are
    not rounded.
    :param probable: Flag. Optional. By default, "False". Accepts only a "True" or a "False". When "True", the
    function returns the likely data.
    :param explanation: Flag. Optional. By default, "False". Accepts only a "True" or a "False". When "True", the
    function returns the string data.
    :param  limitation: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When "False",
    there is no limit.
    :param only_integers: Flag. Optional. By default, "False". Accepts only a "True" or a "False". When "True", step
    becomes 1.
    :return: Returns the computation of class "PythagoreanTheoremClass" based on the parameters you specify.
    """
    if not isinstance(first_leg, int | float | None):
        raise ValueError(f'Parameter "first_leg" error. It accepts only "int" and "float". You asked "{first_leg}"')
    if not isinstance(second_leg, int | float | None):
        raise ValueError(f'Parameter "second_leg" error. It accepts only "int" and "float". You asked "{second_leg}"')
    if not isinstance(hypotenuse, int | float | None):
        raise ValueError(f'Parameter "hypotenuse" error. It accepts only "int" and "float". You asked "{hypotenuse}"')
    if not isinstance(unit, str):
        raise ValueError(f'Parameter "unit" error. It accepts only "str". You asked "{unit}"')
    if not isinstance(sides, bool):
        raise ValueError(f'Parameter "sides" error. It accepts only "True" and "False". You asked "{sides}"')
    if not isinstance(perimeter, bool):
        raise ValueError(f'Parameter "perimeter" error. It accepts only "True" and "False". You asked "{perimeter}"')
    if not isinstance(area, bool):
        raise ValueError(f'Parameter "area" error. It accepts only "True" and "False". You asked "{area}"')
    if not isinstance(rounding, bool):
        raise ValueError(f'Parameter "rounding" error. It accepts only "True" and "False". You asked "{rounding}"')
    if not isinstance(probable, bool):
        raise ValueError(f'Parameter "probable" error. It accepts only "True" and "False". You asked "{probable}"')
    if not isinstance(explanation, bool):
        raise ValueError(
            f'Parameter "explanation" error. It accepts only "True" and "False". You asked "{explanation}"')
    if not isinstance(limitation, bool):
        raise ValueError(f'Parameter "limitation" error. It accepts only "True" and "False". You asked '
                         f'"{limitation}"')
    if not isinstance(only_integers, bool):
        raise ValueError(f'Parameter "only_integers" error. It accepts only "True" and "False". You asked '
                         f'"{only_integers}"')
    if (first_leg is not None
        and first_leg <= 0) \
            or (second_leg is not None
                and second_leg <= 0) \
            or (hypotenuse is not None
                and hypotenuse <= 0):
        raise ValueError(f'Side ({"first leg: " + str(first_leg) if first_leg is not None and first_leg <= 0 else ""}'
                         f'{", " if (first_leg is not None and first_leg <= 0) and ((second_leg is not None and second_leg <= 0) or (hypotenuse is not None and hypotenuse <= 0)) else ""}'
                         f'{"second leg: " + str(second_leg) if second_leg is not None and second_leg <= 0 else ""}'
                         f'{", " if (second_leg is not None and second_leg <= 0) and (hypotenuse is not None and hypotenuse <= 0) else ""}'
                         f'{"hypotenuse: " + str(hypotenuse) if hypotenuse is not None and hypotenuse <= 0 else ""}) '
                         f'length cannot be less than 0 or equal to 0')
    if explanation \
            and limitation:
        print('\nIf the value of any side is greater than 100, the length will automatically be equal to 100. You '
              'will be notified about this. Be careful, you may get an error')
    if limitation:
        if first_leg is not None \
                and first_leg > 100:
            if explanation:
                print(
                    f'\nThe length of the first leg is more than 100 ({first_leg}). It will be automatically equal '
                    f'to 100. An error may occur')
            first_leg: int | float = 100
        if second_leg is not None \
                and second_leg > 100:
            if explanation:
                print(f'\nThe length of the second leg is more than 100 ({second_leg}). It will be automatically '
                      f'equal to 100. An error may occur')
            second_leg: int | float = 100
        if hypotenuse is not None \
                and hypotenuse > 100:
            if explanation:
                print(f'\nThe length of the hypotenuse is more than 100 ({hypotenuse}). It will be automatically '
                      f'equal to 100. An error may occur')
            hypotenuse: int | float = 100
    pythagorean_theorem = PythagoreanTheoremClass(first_leg=first_leg,
                                                  second_leg=second_leg,
                                                  hypotenuse=hypotenuse)
    if hypotenuse is None \
            and first_leg is not None \
            and second_leg is not None \
            and sides:
        hcm: int | float | None = pythagorean_theorem.hypotenuse_calculation_method(rounding)
    if ((first_leg is None
         and second_leg is not None)
        or (second_leg is None
            and first_leg is not None)) \
            and hypotenuse is not None \
            and sides:
        lcm: int | float | None = pythagorean_theorem.leg_calculation_method(rounding)
    if hypotenuse is not None \
            and first_leg is None \
            and second_leg is None \
            and probable \
            and sides:
        plcm: list | None = pythagorean_theorem.probable_legs_calculation_method(rounding,
                                                                                 only_integers)
    if ((first_leg is not None
         and second_leg is None)
        or (second_leg is not None
            and first_leg is None)) \
            and hypotenuse is None \
            and probable \
            and sides:
        if limitation is False:
            print('\nFor sides:')
        phlcm: list | None = pythagorean_theorem.probable_hypotenuse_and_leg_calculation_method(rounding,
                                                                                                limitation,
                                                                                                only_integers)
    if perimeter:
        if ((first_leg is not None
             and second_leg is None)
            or (second_leg is not None
                and first_leg is None)) \
                and hypotenuse is None:
            if limitation is False:
                print('For perimeter:')
        pcm: int | float | list | None = pythagorean_theorem.perimeter_calculation_method(rounding,
                                                                                          limitation,
                                                                                          only_integers)
    if area:
        if ((first_leg is not None
             and second_leg is None)
            or (second_leg is not None
                and first_leg is None)) \
                and hypotenuse is None:
            if limitation is False:
                print('For area:')
        acm: int | float | list | None = pythagorean_theorem.area_calculation_method(rounding,
                                                                                     limitation,
                                                                                     only_integers)
    if hypotenuse is None \
            and first_leg is not None \
            and second_leg is not None \
            and sides \
            and hcm is not None:
        if explanation:
            print(f'\nThe length of the hypotenuse will be calculated with the first leg {first_leg}'
                  f'{unit} and the second leg {second_leg}'
                  f'{unit}. It may take some time, please wait')
            print(f'Hypotenuse: {hcm}'
                  f'{unit}')
        else:
            if unit == '':
                print(hcm)
            else:
                print(f'{hcm}{unit}')
    if ((first_leg is None
         and second_leg is not None)
        or (second_leg is None
            and first_leg is not None)) \
            and hypotenuse is not None \
            and sides \
            and lcm is not None:
        if explanation:
            print(f'\nThe length of the first leg will be calculated with the hypotenuse {hypotenuse}'
                  f'{unit} and the second leg {second_leg}'
                  f'{unit}. It may take some time, please wait'
                  if first_leg is None else
                  f'\nThe length of the second leg will be calculated with the hypotenuse {hypotenuse}'
                  f'{unit} and the first leg {first_leg}'
                  f'{unit}. It may take some time, please wait')
            print(f'First leg: {lcm}{unit}'
                  if first_leg is None else
                  f'Second leg: {lcm}{unit}')
        else:
            if unit == '':
                print(lcm)
            else:
                print(f'{lcm}{unit}')
    if hypotenuse is not None \
            and first_leg is None \
            and second_leg is None \
            and probable \
            and sides \
            and plcm is not None:
        if explanation:
            print(f'\nThe probable lengths of the legs with a hypotenuse of {hypotenuse}'
                  f'{unit} will be calculated. It may take some time, please wait')
            counter: int = 1
            for fl, sl in plcm:
                print(f'{counter}. Probable first leg: {fl}{unit}, Probable second '
                      f'leg: {sl}{unit}')
                counter += 1
        else:
            if unit == '':
                print(plcm)
            else:
                plcm_list: list = []
                for pl, cm in plcm:
                    plcm_list.append((f'{pl}{unit}', f'{cm}{unit}'))
                print(plcm_list)
    if ((first_leg is not None
         and second_leg is None)
        or (second_leg is not None
            and first_leg is None)) \
            and hypotenuse is None \
            and probable \
            and sides \
            and phlcm is not None:
        if explanation:
            print(f'\nThe probable lengths of the hypotenuse and second leg with a first leg of {first_leg}'
                  f'{unit} will be calculated. It may take some time, please wait'
                  if first_leg is not None else
                  f'\nThe probable lengths of the hypotenuse and first leg with a second leg of {second_leg}'
                  f'{unit} will be calculated. It may take some time, please wait')
            counter: int = 1
            for hptns, l in phlcm:
                print(f'{counter}. Probable hypotenuse: {hptns}{unit}, Probable second '
                      f'leg: {l}{unit}' if first_leg is not None else
                      f'{counter}. Probable hypotenuse: {hptns}{unit}, Probable first '
                      f'leg: {l}{unit}')
                counter += 1
        else:
            if unit == '':
                print(phlcm)
            else:
                phlcm_list: list = []
                for phl, cm in phlcm:
                    phlcm_list.append((f'{phl}{unit}', f'{cm}{unit}'))
                print(phlcm_list)
    if (perimeter
        or area) \
            and explanation:
        if (first_leg is not None
            and second_leg is not None) \
                or (first_leg is not None
                    and hypotenuse is not None) \
                or (second_leg is not None
                    and hypotenuse is not None):
            accurate_string = f'will be calculated with ' \
                              f'{first_leg if first_leg is not None else PythagoreanTheoremClass(second_leg=second_leg, hypotenuse=hypotenuse).leg_calculation_method(rounding)}' \
                              f'{unit} first leg, ' \
                              f'{second_leg if second_leg is not None else PythagoreanTheoremClass(first_leg=first_leg, hypotenuse=hypotenuse).leg_calculation_method(rounding)}' \
                              f'{unit} second leg and ' \
                              f'{hypotenuse if hypotenuse is not None else PythagoreanTheoremClass(first_leg=first_leg, second_leg=second_leg).hypotenuse_calculation_method(rounding)}' \
                              f'{unit} hypotenuse'
        if probable:
            probable_string = f'will be calculated ' \
                              f'with the side known to us ' \
                              f'({"hypotenuse: " + str(hypotenuse) if hypotenuse is not None else ""}' \
                              f'{"first leg: " + str(first_leg) if first_leg is not None else ""}' \
                              f'{"second leg: " + str(second_leg) if second_leg is not None else ""}' \
                              f'{unit}). It may take some time, please wait'
    if perimeter \
            and pcm is not None:
        if explanation:
            if ((first_leg is None
                 and second_leg is None)
                or (first_leg is None
                    and hypotenuse is None)
                or (second_leg is None
                    and hypotenuse is None)) \
                    and probable:
                print('\nThe probable perimeters ' + probable_string)
                counter: int = 1
                for p in pcm:
                    print(f'{counter}. Probable perimeter: {p}{unit}')
                    counter += 1
            elif (first_leg is not None
                  and second_leg is not None) \
                    or (first_leg is not None
                        and hypotenuse is not None) \
                    or (second_leg is not None
                        and hypotenuse is not None):
                print('\nThe perimeter ' + accurate_string)
                print(f'Perimeter: {pcm}'
                      f'{unit if unit is not None else ""}')
        else:
            if isinstance(pcm, list) \
                    and probable:
                if unit == '':
                    print(pcm)
                else:
                    perimeter_list: list = []
                    for p in pcm:
                        perimeter_list.append(f'{p}{unit}')
                    print(perimeter_list)
            elif not isinstance(pcm, list):
                if unit == '':
                    print(pcm)
                else:
                    print(f'{pcm}{unit}')

    if area \
            and acm is not None:
        two_in_index: str = '\u00B2'
        if explanation:
            if ((first_leg is None
                 and second_leg is None)
                or (first_leg is None
                    and hypotenuse is None)
                or (second_leg is None
                    and hypotenuse is None)) \
                    and probable:
                print('\nThe probable areas ' + probable_string)
                counter: int = 1
                for a in acm:
                    print(f'{counter}. Probable area: {a}{unit + two_in_index if unit != "" else ""}')
                    counter += 1
            elif (first_leg is not None
                  and second_leg is not None) \
                    or (first_leg is not None
                        and hypotenuse is not None) \
                    or (second_leg is not None
                        and hypotenuse is not None):
                print('\nThe area ' + accurate_string)
                print(
                    f'Area: {acm}'
                    f'{unit + two_in_index if unit is not None else ""}')
        else:
            if isinstance(acm, list) \
                    and probable:
                if unit == '':
                    print(acm)
                else:
                    area_list: list = []
                    for a in acm:
                        area_list.append(f'{a}{unit + two_in_index}')
                    print(area_list)
            elif not isinstance(acm, list):
                if unit == '':
                    print(acm)
                else:
                    print(f'{acm}{unit + two_in_index}')


def pythagorean_theorem_run_function(*, first_leg: int | float | None = None,
                                     second_leg: int | float | None = None,
                                     hypotenuse: int | float | None = None,
                                     unit: str = '',
                                     sides: bool = True,
                                     perimeter: bool = False,
                                     area: bool = False,
                                     rounding: bool = True,
                                     probable: bool = False,
                                     explanation: bool = False,
                                     limitation: bool = True,
                                     only_integers: bool = False,
                                     automatic_parameters: bool = True,
                                     all_meanings: bool = False):
    """
    This function is auxiliary for working with the "pythagorean_theorem_function" function. It is very easy to use.
    You just have to specify the parameters you need.
    :param first_leg: The first leg of a right-angled triangle. Optional. By default, "None". Accepts only integers or
    real numbers.
    :param second_leg: The second leg of a right-angled triangle. Optional. By default, "None". Accepts only integers
    or real numbers.
    :param hypotenuse: The hypotenuse of a right-angled triangle. Optional. By default, "None". Accepts only integers
    or real numbers.
    :param unit: Measurement value. Optional. By default, "". Accepts only a string.
    :param sides: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When "False", neither side is
    evaluated.
    :param perimeter: Flag. Optional. By default, "False". Accepts only a "True" or a "False". When "True", the
    perimeter is calculated.
    :param area: Flag. Optional. By default, "False". Accepts only a "True" or a "False". When "True", the area is
    calculated.
    :param rounding: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When "False", numbers are
    not rounded.
    :param probable: Flag. Optional. By default, "False". Accepts only a "True" or a "False". When "True", the
    function returns the likely data.
    :param explanation: Flag. Optional. By default, "False". Accepts only a "True" or a "False". When "True", the
    function returns the string data.
    :param  limitation: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When "False",
    there is no limit.
    :param only_integers: Flag. Optional. By default, "False". Accepts only a "True" or a "False". When "True", step
    becomes 1.
    :param automatic_parameters: Flag. Optional. By default, "True". Accepts only a "True" or a "False". When "False",
    behaves like a function "pythagorean_theorem_function".
    :param all_meanings: Flag. Optional. By default, "False". Accepts only a "True" or a "False". When "True", all
    available information is shown.
    :return: Returns the computation of function "pythagorean_theorem_function" based on the parameters you specify.
    """
    if not isinstance(automatic_parameters, bool):
        raise ValueError(f'Parameter "automatic_parameters" error. It accepts only "True" and "False". You asked '
                         f'"{automatic_parameters}"')
    if not isinstance(all_meanings, bool):
        raise ValueError(f'Parameter "all_meanings" error. It accepts only "True" and "False". You asked '
                         f'"{all_meanings}"')
    if all_meanings:
        automatic_parameters = False
        perimeter = True
        area = True
        rounding = False
        probable = True
        explanation = True
        limitation = False
    if automatic_parameters:
        if first_leg is not None \
                and second_leg is not None \
                and hypotenuse is not None \
                and sides is True:
            sides = False
        if first_leg is not None \
                and second_leg is not None \
                and hypotenuse is not None \
                and perimeter is False \
                and area is False:
            question: str = input('\nYou have specified the length of all sides. What do you want to calculate?'
                                  '\nIf you want only perimeter, just write 0 and press "Enter"'
                                  '\nIf you want only area, just write 1 and press "Enter"'
                                  '\nIf you want perimeter and area, just write 10 and press "Enter"'
                                  '\nYour choice: ')
            match question:
                case '0':
                    perimeter = True
                case '1':
                    area = True
                case '10':
                    perimeter = True
                    area = True
        if (first_leg is None
            and second_leg is None) \
                or (first_leg is None
                    and hypotenuse is None) \
                or (second_leg is None
                    and hypotenuse is None) \
                and probable is False:
            probable = True
        if unit != '' \
                and explanation is False:
            select_unit: str = input(f'\nYou have specified the unit "{unit}".'
                                     '\nWant to include an explanation?'
                                     '\nIf you want, just write 0 and press "Enter": ')
            if select_unit == '0':
                explanation = True
            else:
                print('\n')
        if limitation is True:
            if (first_leg is not None
                and first_leg > 100) \
                    or (second_leg is not None
                        and second_leg > 100) \
                    or (hypotenuse is not None
                        and hypotenuse > 100):
                clarification: str = input('\nYou have set a value greater than 100. Want to turn off'
                                           '"limitation"?.'
                                           '\nIf you want, just write 0 and press "Enter" (be careful, an error may'
                                           'occur): ')
                if clarification == '0':
                    limitation = False
        if limitation is True:
            if (first_leg is not None
                and second_leg is None
                and hypotenuse is None) \
                    or (second_leg is not None
                        and first_leg is None
                        and hypotenuse is None):
                clarification: str = input('\nYou have specified the length of only one leg. The process of '
                                           'calculating probable values can take a long time. Want to turn off '
                                           'limitation?'
                                           '\nIf you want, just write 0 and press "Enter" (be careful, an error may'
                                           'occur): ')
                if clarification == '0':
                    limitation = False
    pythagorean_theorem_function(first_leg=first_leg,
                                 second_leg=second_leg,
                                 hypotenuse=hypotenuse,
                                 unit=unit,
                                 sides=sides,
                                 perimeter=perimeter,
                                 area=area,
                                 rounding=rounding,
                                 probable=probable,
                                 explanation=explanation,
                                 limitation=limitation,
                                 only_integers=only_integers)


if __name__ == '__main__':
    print('\nRun function')
    pythagorean_theorem_run_function(
        first_leg=3,
        second_leg=4,
        hypotenuse=5,
        unit='cm',
        sides=True,
        perimeter=False,
        area=False,
        rounding=True,
        probable=False,
        explanation=False,
        limitation=True,
        only_integers=False,
        automatic_parameters=True,
        all_meanings=False
    )
    print('\nEnd function')
