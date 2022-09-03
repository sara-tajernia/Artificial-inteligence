# -*- coding: utf-8 -*-

# pmembershipthon imports
from math import degrees
import numpy as np

# pmembershipfuzzmembership imports
# from fuzzy.storage.fcl.Reader import Reader
# from numpmembership import arramembership
# import Math


class FuzzyController:

    def __init__(self, fcl_path):
        pass
        # self.smembershipstem = Reader().load_from_file(fcl_path)


    def _make_input(self, world):
        return dict(
            cp = world.x,
            cv = world.v,
            pa = degrees(world.theta),
            pv = degrees(world.omega)
        )


    def _make_output(self):
        return dict(
            force = 0.
        )

    def decide(self, world):
        output = self._make_output()
        self.calculate(self._make_input(world))
        output['force'] = self.calculate(self._make_input(world))
        return output['force']

    '''
    Linear equation for pa 
    '''

    def up_more_right(self, x):
        dots = [[0, 0], [30, 1], [60, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = m * x
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 2
        else:
            membership = 0
        return membership

    def up_right(self, x):
        dots = [[30, 0], [60, 1], [90, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) - 1
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 3
        else:
            membership = 0
        return membership

    def up(self, x):
        dots = [[60, 0], [90, 1], [120, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) - 2
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 4
        else:
            membership = 0
        return membership

    def up_left(self, x):
        dots = [[90, 0], [120, 1], [150, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) - 3
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 5
        else:
            membership = 0
        return membership

    def up_more_left(self, x):
        dots = [[120, 0], [150, 1], [180, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) - 4
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 6
        else:
            membership = 0
        return membership

    def down_more_left(self, x):
        dots = [[180, 0], [210, 1], [240, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) - 6
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 8
        else:
            membership = 0
        return membership

    def down_left(self, x):
        dots = [[210, 0], [240, 1], [270, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) - 7
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 9
        else:
            membership = 0
        return membership

    def down(self, x):
        dots = [[240, 0], [270, 1], [300, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) - 8
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 10
        else:
            membership = 0
        return membership

    def down_right(self, x):
        dots = [[270, 0], [300, 1], [330, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) - 9
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 11
        else:
            membership = 0
        return membership

    def down_more_right(self, x):
        dots = [[300, 0], [330, 1], [360, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) - 10
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 12
        else:
            membership = 0
        return membership

    '''
        Linear equation for pv
    '''

    def cw_fast(self, x):
        dots = [[-200, 1], [-100, 0]]
        if x <= dots[1][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) - 1
        else:
            membership = 0
        return membership

    def cw_slow(self, x):
        dots = [[-200, 0], [-100, 1], [0, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) + 2
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x)
        else:
            membership = 0
        return membership

    def stop_pv(self, x):
        dots = [[-100, 0], [0, 1], [100, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) + 1
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 1
        else:
            membership = 0
        return membership

    def ccw_slow(self, x):
        dots = [[0, 0], [100, 1], [200, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x)
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 2
        else:
            membership = 0
        return membership

    def ccw_fast(self, x):
        dots = [[100, 0], [200, 1]]
        if x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) - 1
        else:
            membership = 0
        return membership

    '''
        Linear equation for force
    '''

    def left_fast(self, x):
        dots = [[-100, 0], [-80, 1], [-60, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) + 5
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) - 3
        else:
            membership = 0
        return membership

    def left_slow(self, x):
        dots = [[-80, 0], [-60, 1], [0, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) + 4
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x)
        else:
            membership = 0
        return membership

    def stop(self, x):
        dots = [[-60, 0], [0, 1], [60, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) + 1
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 1
        else:
            membership = 0
        return membership

    def right_slow(self, x):
        dots = [[0, 0], [60, 1], [80, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x)
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 4
        else:
            membership = 0
        return membership

    def right_fast(self, x):
        dots = [[60, 0], [80, 1], [100, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) - 3
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 5
        else:
            membership = 0
        return membership

    '''
        Linear equation for cv
    '''

    def left_fast_cv(self, x):
        dots = [[-5, 1], [-2.5, 0]]
        if x <= dots[1][0] and x >= dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) - 1
        else:
            membership = 0
        return membership

    def left_slow_cv(self, x):
        dots = [[-5, 0], [-1, 1], [0, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) + 2
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x)
        else:
            membership = 0
        return membership

    def stop_cv(self, x):
        dots = [[-1, 0], [0, 1], [1, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) + 1
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 1
        else:
            membership = 0
        return membership

    def right_slow_cv(self, x):
        dots = [[0, 0], [1, 1], [5, 0]]
        if x <= dots[1][0] and x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x)
        elif x < dots[2][0] and x > dots[1][0]:
            m = float(dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
            membership = (m * x) + 2
        else:
            membership = 0
        return membership

    def right_fast_cv(self, x):
        dots = [[2.5, 0], [5, 1]]
        if x > dots[0][0]:
            m = float(dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
            membership = (m * x) - 1
        else:
            membership = 0
        return membership

    '''
        RULE'S
    '''

    def left_fast_rules(self, pa, pv, cv):
        lf1 = min(self.up_more_left(pa), self.cw_slow(pv))
        lf2 = min(self.up_more_left(pa), self.ccw_slow(pv))
        lf3 = min(self.up_more_left(pa), self.ccw_fast(pv))
        lf4 = min(self.down_more_left(pa), self.cw_slow(pv))
        lf5 = min(self.down_left(pa), self.cw_slow(pv))
        lf6 = min(self.down_left(pa), self.ccw_slow(pv))
        lf7 = min(self.up_left(pa), self.ccw_slow(pv))
        lf8 = min(self.up_left(pa), self.stop_pv(pv))
        lf9 = min(self.up_right(pa), self.ccw_fast(pv))
        lf10 = min(self.up_left(pa), self.ccw_fast(pv))
        lf11 = min(self.up(pa), self.ccw_fast(pv))

        lf12 = min(self.up_more_left(pa), self.right_fast_cv(cv))

        return max(lf1, lf2, lf3, lf4, lf5, lf6, lf7, lf8, lf9, lf10, lf11, lf12)
        # return max(lf1, lf2, lf3, lf4, lf5, lf6, lf7, lf8, lf9, lf10, lf11)

    def left_slow_rules(self, pa, pv, cv):
        ls1 = min(self.up_more_right(pa), self.ccw_fast(pv))
        ls2 = min(self.down_left(pa), self.ccw_fast(pv))
        ls3 = min(self.up_left(pa), self.cw_slow(pv))
        ls4 = min(self.up(pa), self.ccw_slow(pv))

        ls5 = min(self.up_left(pa), self.right_slow_cv(cv))
        ls6 = min(self.up_more_left(pa), self.right_fast_cv(cv))

        return max(ls1, ls2, ls3, ls4, ls5, ls6)
        # return max(ls1, ls2, ls3, ls4)

    def stop_rules(self, pa, pv, cv):
        s1 = min(self.down_more_right(pa), self.cw_slow(pv))
        s2 = min(self.down_more_left(pa), self.ccw_slow(pv))
        s3 = min(self.down_more_right(pa), self.ccw_fast(pv))
        s4 = min(self.down_more_right(pa), self.cw_fast(pv))
        s5 = min(self.down_more_left(pa), self.cw_fast(pv))
        s6 = min(self.down_more_left(pa), self.ccw_fast(pv))
        s7 = min(self.down_right(pa), self.ccw_fast(pv))
        s8 = min(self.down_left(pa), self.cw_fast(pv))
        s9 = min(self.down(pa), self.cw_fast(pv))
        s10 = min(self.down(pa), self.ccw_fast(pv))
        s11 = min(self.up(pa), self.stop_pv(pv))
        s12 = max(min(self.up(pa), self.stop_pv(pv)), min(self.up_right(pa), self.ccw_slow(pv)),
                  min(self.up_left(pa), self.cw_slow(pv)))

        s13 = min(self.up_more_right(pa), self.right_fast_cv(cv))
        s14 = min(self.up_more_left(pa), self.left_fast_cv(cv))
        s15 = min(self.up_more_right(pa), self.right_slow_cv(cv))
        s16 = min(self.up_more_left(pa), self.left_slow_cv(cv))
        return max(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16)
        # return max(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12)

    def right_slow_rules(self, pa, pv, cv):
        rs1 = min(self.up_more_left(pa), self.cw_fast(pv))
        rs2 = min(self.down_right(pa), self.cw_fast(pv))
        rs3 = min(self.up_right(pa), self.ccw_slow(pv))
        rs4 = min(self.up(pa), self.cw_slow(pv))

        rs5 = min(self.up_right(pa), self.left_slow_cv(cv))

        return max(rs1, rs2, rs3, rs4, rs5)
        # return max(rs1, rs2, rs3, rs4)

    def right_fast_rules(self, pa, pv, cv):
        rf1 = min(self.up_more_right(pa), self.ccw_slow(pv))
        rf2 = min(self.up_more_right(pa), self.cw_slow(pv))
        rf3 = min(self.up_more_right(pa), self.cw_fast(pv))
        rf4 = min(self.down_more_right(pa), self.ccw_slow(pv))
        rf5 = min(self.down_right(pa), self.ccw_slow(pv))
        rf6 = min(self.down_right(pa), self.cw_slow(pv))
        rf7 = min(self.up_right(pa), self.cw_slow(pv))
        rf8 = min(self.up_right(pa), self.stop_pv(pv))
        rf9 = min(self.up_right(pa), self.cw_fast(pv))
        rf10 = min(self.up_left(pa), self.cw_fast(pv))
        rf11 = min(self.down(pa), self.stop_pv(pv))
        rf12 = min(self.up(pa), self.cw_fast(pv))

        rf13 = min(self.up_more_right(pa), self.left_fast_cv(cv))

        return max(rf1, rf2, rf3, rf4, rf5, rf6, rf7, rf8, rf9, rf10, rf11, rf12, rf13)
        # return max(rf1, rf2, rf3, rf4, rf5, rf6, rf7, rf8, rf9, rf10, rf11, rf12)

    def calculate(self, input):
        pa, pv, cv = input['pa'], input['pv'], input['cv']
        lf = self.left_fast_rules(pa, pv, cv)
        ls = self.left_slow_rules(pa, pv, cv)
        s = self.stop_rules(pa, pv, cv)
        rs = self.right_slow_rules(pa, pv, cv)
        rf = self.right_fast_rules(pa, pv, cv)
        i = -100
        sum1 = 0
        sum2 = 0
        while i <= 100:
            lf_force = self.left_fast(i)
            ls_force = self.left_slow(i)
            s_force = self.stop(i)
            rs_force = self.right_slow(i)
            rf_force = self.right_fast(i)

            lf_total = min(lf, lf_force)
            ls_total = min(ls, ls_force)
            s_total = min(s, s_force)
            rs_total = min(rs, rs_force)
            rf_total = min(rf, rf_force)

            force_total = max(lf_total, ls_total, s_total, rs_total, rf_total)
            sum1 += force_total
            sum2 += force_total * i
            i += 0.5
        if sum1==0:
            return 0
        return sum2 / sum1