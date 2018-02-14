import unittest

from prob02_algospot_pi.pi import minimum_level


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_end2end_1(self):
        q1 = "12341234"
        self.assertEqual(4, minimum_level(q1))

    def test_end2end_2(self):
        q1 = "11111222"
        self.assertEqual(2, minimum_level(q1))

    def test_end2end_3(self):
        q1 = "12122222"
        self.assertEqual(5, minimum_level(q1))

    def test_end2end_4(self):
        q1 = "22222222"
        self.assertEqual(2, minimum_level(q1))

    def test_end2end_5(self):
        q1 = "12673939"
        self.assertEqual(14, minimum_level(q1))




if __name__ == '__main__':
    unittest.main()


"""
    가끔 TV 에 보면 원주율을 몇만 자리까지 줄줄 외우는 신동들이 등장하곤 합니다.
    이들이 이 수를 외우기 위해 사용하는 방법 중 하나로, 숫자를 몇 자리 이상 끊어 외우는 것이 있습니다.
    이들은 숫자를 세 자리에서 다섯 자리까지로 끊어서 외우는데, 
    가능하면 55555 나 123 같이 외우기 쉬운 조각들이 많이 등장하는 방법을 택하곤 합니다.
    
    이 때, 각 조각들의 난이도는 다음과 같이 정해집니다:
    
    모든 숫자가 같을 때 (예: 333, 5555) 난이도: 1
    숫자가 1씩 단조 증가하거나 단조 감소할 때 (예: 23456, 3210) 난이도: 2
    두 개의 숫자가 번갈아 가며 출현할 때 (예: 323, 54545) 난이도: 4
    숫자가 등차 수열을 이룰 때 (예: 147, 8642) 난이도: 5
    그 외의 경우 난이도: 10
    
    원주율의 일부가 입력으로 주어질 때, 난이도의 합을 최소화하도록 숫자들을 
    3자리에서 5자리까지 끊어 읽고 싶습니다. 최소의 난이도를 계산하는 프로그램을 작성하세요.
    
    입력
    입력의 첫 줄에는 테스트 케이스의 수 C (<= 50) 가 주어집니다.
    각 테스트 케이스는 8글자 이상 10000글자 이하의 숫자로 주어집니다.
    
    출력
    각 테스트 케이스마다 한 줄에 최소의 난이도를 출력합니다.
"""