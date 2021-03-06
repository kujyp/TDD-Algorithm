import io
import unittest
from unittest.mock import patch

from probs.prob05_routing.routing import main

"""

문제
judge-attachments/97b28a9bc67d610b59be1fc7e9a39841/delivery7.png

위 그림은 여러 개의 컴퓨터들과 각 컴퓨터들을 잇는 회선을 나타냅니다. 각 회선들은 각각 품질이 다르며, 각 회선을 지날 때마다 신호에
있던 노이즈가 증폭될 수 있습니다. 각 회선에 쓰여 있는 글자는 해당 회선을 지날 때 노이즈가 몇 배 증폭되는가를 보여줍니다. 특정
컴퓨터에서 다른 컴퓨터로 메시지를 보내고 싶습니다. 이 때 노이즈의 증폭을 최소화하는 프로그램을 작성하세요.

입력
입력의 첫 줄에는 테스트 케이스의 수 C (<= 50) 이 주어집니다. 각 테스트 케이스의 첫 줄에는 컴퓨터의 수 N (<= 10000) 과
회선의 수 M (<= 20000) 이 주어집니다. 각 컴퓨터는 0 부터 N-1 까지의 번호로 표현됩니다. 그 후 줄에 각 3개의 정수로 각
회선의 정보가 주어집니다. 회선의 정보는 a b c 로 표현되며, 이 때 이 회선은 a 번과 b 번 컴퓨터 사이를 이으며 이 회선을 지날 때
노이즈는 c 배 증폭됩니다. c 는 언제나 1 이상의 실수입니다. 모든 회선은 양방향으로 데이터를 전송할 수 있습니다.

시작
컴퓨터는 항상 0 번, 끝 컴퓨터는 항상 N-1번이라고 가정하며, 이와 같은 경로는 언제나 존재한다고 가정합니다.

출력
각 테스트 케이스마다, 노이즈가 최소화되는 경로에서 노이즈는 몇 배로 증폭되는지를 소숫점 밑 열 자리까지
출력합니다. 10^-7 이상의 상대/절대 오차가 허용됩니다.


"""


class RoutingTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_end2end_1(self, captured_output):
        raw_input = """\
1
7 14
0 1 1.3
0 2 1.1
0 3 1.24
3 4 1.17
3 5 1.24
3 1 2
1 2 1.31
1 2 1.26
1 4 1.11
1 5 1.37
5 4 1.24
4 6 1.77
5 6 1.11
2 6 1.2
"""
        user_input = raw_input.split("\n")

        with patch('builtins.input', side_effect=user_input):
            main()
            output = captured_output.getvalue()
            output = output.rstrip()

        self.assertEqual("1.3200000000", output)


class Array(unittest.TestCase):
    def test_str2int_array(self):
        from probs.prob05_routing.routing import str2int_array
        [arg1, arg2] = str2int_array("7 14")
        self.assertEqual(type(arg1), int)
        self.assertEqual(type(arg2), int)
        self.assertEqual(arg1, 7)
        self.assertEqual(arg2, 14)

    def test_str2int_or_float_array(self):
        from probs.prob05_routing.routing import str2int_or_float_array
        [arg1, arg2, arg3] = str2int_or_float_array("0 1 1.3")
        self.assertEqual(type(arg1), int)
        self.assertEqual(type(arg2), int)
        self.assertEqual(type(arg3), float)
        self.assertEqual(arg1, 0)
        self.assertEqual(arg2, 1)
        self.assertEqual(arg3, 1.3)
