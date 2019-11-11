class MergeSort:

    def sort(self, l: list) -> list:
        if len(l) <= 1:
            return l

        a, b = self.sort(l[0::2]), self.sort(l[1::2])

        return self.__merge_lists(a, b)
    
    def __merge_lists(self, a: list, b: list) -> list:

        result = list()
        i = j = k = 0

        len_a, len_b = len(a), len(b)

        while k < (len_a + len_b):

            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1

            if i == len_a:
                result += b[j:]
                break

            if j == len_b:
                result += a[i:]
                break

            k += 1

        return result


def user_input_to_int_list(input_string: str) -> list:
    result = list()

    for s in input_string:

        try:
            int(s)
            result.append(s)
        except ValueError:
            continue

    return result


if __name__ == "__main__":
    sort = MergeSort()

    list_of_ints = user_input_to_int_list(input('Type some numbers to sort them' + "\n"))

    print(sort.sort(list_of_ints))
