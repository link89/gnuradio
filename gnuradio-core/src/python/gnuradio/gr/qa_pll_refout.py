#!/usr/bin/env python
#
# Copyright 2004,2010 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr, gr_unittest
import math

class test_pll_refout (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block()

    def tearDown (self):
        self.tb = None

    def test_pll_refout (self):
        expected_result = ((1+0j),
                           (1+6.4087357643e-10j),
                           (0.999985277653+0.00542619498447j),
                           (0.999868750572+0.0162021834403j),
                           (0.99948567152+0.0320679470897j),
                           (0.99860727787+0.0527590736747j),
                           (0.996953129768+0.0780025869608j),
                           (0.994203746319+0.107512556016j),
                           (0.990011692047+0.140985429287j),
                           (0.984013140202+0.178095817566j),
                           (0.975838363171+0.218493551016j),
                           (0.965121984482+0.261800557375j),
                           (0.95151245594+0.307610183954j),
                           (0.934681296349+0.355486690998j),
                           (0.914401650429+0.404808044434j),
                           (0.890356600285+0.455263823271j),
                           (0.862329125404+0.506348133087j),
                           (0.830152392387+0.557536482811j),
                           (0.793714106083+0.608290970325j),
                           (0.752960026264+0.658066213131j),
                           (0.707896590233+0.706316053867j),
                           (0.658591926098+0.752500295639j),
                           (0.605175673962+0.796091973782j),
                           (0.547837555408+0.836584687233j),
                           (0.48682525754+0.873499393463j),
                           (0.42244040966+0.906390726566j),
                           (0.355197101831+0.934791445732j),
                           (0.285494059324+0.958380460739j),
                           (0.213591173291+0.976923108101j),
                           (0.139945343137+0.990159213543j),
                           (0.065038472414+0.997882783413j),
                           (-0.0106285437942+0.999943494797j),
                           (-0.0865436866879+0.996248066425j),
                           (-0.162189796567+0.986759603024j),
                           (-0.23705175519+0.971496999264j),
                           (-0.310622543097+0.950533330441j),
                           (-0.38240903616+0.923993110657j),
                           (-0.451937526464+0.89204955101j),
                           (-0.518758952618+0.854920566082j),
                           (-0.582311093807+0.812966048717j),
                           (-0.642372369766+0.76639264822j),
                           (-0.698591887951+0.715520322323j),
                           (-0.750654160976+0.660695314407j),
                           (-0.798280358315+0.602286040783j),
                           (-0.841228663921+0.540679454803j),
                           (-0.87929558754+0.476276367903j),
                           (-0.912315964699+0.409486919641j),
                           (-0.940161883831+0.340728074312j),
                           (-0.962742805481+0.270418733358j),
                           (-0.980004072189+0.198977485299j),
                           (-0.991925954819+0.126818284392j),
                           (-0.99851256609+0.0545223206282j),
                           (-0.999846458435-0.0175215266645j),
                           (-0.996021270752-0.0891158208251j),
                           (-0.987133920193-0.159895718098j),
                           (-0.973306238651-0.2295101583j),
                           (-0.954683184624-0.297624111176j),
                           (-0.931430280209-0.363919824362j),
                           (-0.903732538223-0.428097635508j),
                           (-0.871792256832-0.489875763655j),
                           (-0.835827112198-0.548992812634j),
                           (-0.796068251133-0.605206847191j),
                           (-0.752758979797-0.658296227455j),
                           (-0.706152498722-0.70805978775j),
                           (-0.656641483307-0.754202902317j),
                           (-0.604367733002-0.79670548439j),
                           (-0.549597978592-0.835429251194j),
                           (-0.492602348328-0.870254516602j),
                           (-0.433654457331-0.901079237461j),
                           (-0.373029649258-0.927819430828j),
                           (-0.31100410223-0.950408577919j),
                           (-0.247853919864-0.968797445297j),
                           (-0.183855071664-0.982953369617j),
                           (-0.119282215834-0.992860376835j),
                           (-0.0544078871608-0.998518764973j),
                           (0.0104992967099-0.999944865704j),
                           (0.0749994292855-0.997183561325j),
                           (0.138844624162-0.990314185619j),
                           (0.201967850327-0.979392170906j),
                           (0.264124274254-0.964488625526j),
                           (0.325075358152-0.945688128471j),
                           (0.3845885396-0.92308807373j),
                           (0.442438393831-0.89679890871j),
                           (0.498407125473-0.866943061352j),
                           (0.552284479141-0.833655714989j),
                           (0.603869199753-0.797083437443j),
                           (0.652970373631-0.757383465767j),
                           (0.69940674305-0.714723825455j),
                           (0.743007957935-0.66928255558j),
                           (0.78350687027-0.62138313055j),
                           (0.820889055729-0.571087777615j),
                           (0.855021059513-0.51859331131j),
                           (0.885780930519-0.46410369873j),
                           (0.913058102131-0.407829582691j),
                           (0.936754107475-0.349988251925j),
                           (0.956783294678-0.290801793337j),
                           (0.973072886467-0.230497643352j),
                           (0.985563337803-0.169307261705j),
                           (0.9942086339-0.1074674353j),
                           (0.9989772439-0.0452152714133j))

        sampling_freq = 10e3
        freq = sampling_freq / 100

        loop_bw = math.pi/100.0
        maxf = 1
        minf = -1

        src = gr.sig_source_c (sampling_freq, gr.GR_COS_WAVE, freq, 1.0)
        pll = gr.pll_refout_cc(loop_bw, maxf, minf)
        head = gr.head (gr.sizeof_gr_complex, int (freq))
        dst = gr.vector_sink_c ()

        self.tb.connect (src, pll, head)
        self.tb.connect (head, dst)

        self.tb.run ()
        dst_data = dst.data ()
        self.assertComplexTuplesAlmostEqual (expected_result, dst_data, 4)

if __name__ == '__main__':
    gr_unittest.run(test_pll_refout, "test_pll_refout.xml")
