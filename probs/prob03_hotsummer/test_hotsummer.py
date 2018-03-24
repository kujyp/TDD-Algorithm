import unittest

from probs.prob03_hotsummer.hotsummer import is_lower_than_or_equal_to_limit

"""
문제
점점 더워지는 여름! 가뜩이나 집에서 바깥바람과 선풍기만으로 더위를 이겨내려고 하는 대학원생 LIBe에게 근무 시간 내내 에어컨을 틀 수
 있었던 연구실은 지상낙원이었다.

어느 날 갑자기 연구실에 근로학생이 찾아와 청천벽력 같은 소식을 전했다. 교내 전체 전력 사용량 감축을 위해 학교 모든 연구실에서
특정시간 동안 에어컨 가동을 중단하기로 했다는 이야기였다.

이야기를 듣자마자 시설팀에 전화를 걸어 항의를 해보았지만, 시설팀에서는 전기 사용량을 정부가 제시한 목표량 이상으로 감축하지 못할
경우 많은 벌금이 부과되기 때문에 어쩔 수 없다는 말만 되풀이할 뿐이었다. 더위를 못 이겨 몰래 에어컨을 켜면 금세 근로학생이 나타나
에어컨을 끄는 것을 부탁하느라 이마저도 포기했다.

이러한 날이 계속되던 와중에, 마침 시설팀에서 감축 정책 개시 이후 첫날의 건물별 시간당 전기 사용량을 알리는 공지 메일을 보냈고,
이를 본 LIBe는 과연 학교에서 정한 감축 정책이 정말 실효를 거두고 있는지를 확인해보려 한다. 메일에는 건물별 목표 전력 사용량과
9시부터 18시까지의 시간대별 전력 사용량이 적혀있다. 이를 토대로 건물별로 목표하는 전력 사용량을 지켰는지를 확인하는 프로그램을 작성하라.

입력
입력의 첫째 줄에는 교내 건물의 수를 뜻하는 숫자 T가 입력된다.

그다음 줄부터 총 T개의 건물의 전력 사용량에 대한 정보가 입력되는데, 이는 두 줄로 이뤄진다. 첫째 줄은 해당 건물의 목표 전력 사용량인
W가 입력되고, 둘째 줄에는 총 9개의 숫자 A9, A10, ..., A17가 입력되는데, Ai는 i 시부터 i+1 시까지의 전력 사용량을
뜻한다. 전력 사용량에서 입력되는 숫자는 모두 0 이상 1,000 이하의 정수이며, 숫자는 공백으로 구분된다.

출력
각 건물에 대해 입력된 순서대로 전체 전력 사용량의 합이 목표 사용량 이하일 경우 "YES"를, 그렇지 못할 경우에는 "NO"를 한 줄에
출력한다.

예제 입력
3
90
10 10 10 10 10 10 10 10 10
1000
77 77 70 11 34 35 41 83 54
50
10 20 30 40 50 60 50 40 30
예제 출력
YES
YES
NO

"""


class HotSummerTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_end2end_1(self):
        limit = 90
        usage = [
            10, 10, 10,
            10, 10, 10,
            10, 10, 10,
        ]
        self.assertEqual("YES", is_lower_than_or_equal_to_limit(limit, usage))

    def test_end2end_2(self):
        limit = 1000
        usage = [
            77, 77, 77,
            11, 34, 35,
            41, 83, 54,
        ]
        self.assertEqual("YES", is_lower_than_or_equal_to_limit(limit, usage))

    def test_end2end_3(self):
        limit = 50
        usage = [
            10, 20, 30,
            40, 50, 60,
            50, 40, 30,
        ]
        self.assertEqual("NO", is_lower_than_or_equal_to_limit(limit, usage))


class Str2IntArray(unittest.TestCase):
    def test_str2int_array(self):
        from probs.prob03_hotsummer.hotsummer import str2int_array
        string = "10 10 10 10 10 10 10 10 10"

        self.assertEqual([
            10, 10, 10,
            10, 10, 10,
            10, 10, 10,
        ], str2int_array(string))
