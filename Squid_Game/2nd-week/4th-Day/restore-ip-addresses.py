class Solution:
	def restoreIpAddresses(self, s: str) -> List[str]:

		ans = []

		if len(s) > 12:
			return []

		def BackTrack(index, dots, current_ip):

			if dots == 4 and index == len(s):
				ans.append(current_ip[:-1])
				return

			if dots > 4:
				return

			for next_index in range(index, min(index + 3, len(s))):

				if int(s[index:next_index + 1]) < 256 and (index == next_index or s[index] != '0'):

					BackTrack(next_index + 1, dots + 1, current_ip + s[index:next_index + 1] + '.')

		BackTrack(0, 0, '')

		return ans