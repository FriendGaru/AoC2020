TEST_CARD = 5764801
TEST_DOOR = 17807724

INPUT_CARD = 12092626
INPUT_DOOR = 4707356


def transform(subject_num, val):
    val *= subject_num
    val %= 20201227
    return val


def loopify(start_val, subject_num, target_num):
    max_loops = 10000000000
    loop_count = 0
    val = start_val
    while not val == target_num and loop_count < max_loops:
        val = transform(subject_num, val)
        loop_count += 1
        # print(loop_count, val)
    return loop_count


def gen_encryption(start_val, subject_num, loops):
    val = start_val
    while loops > 0:
        loops -= 1
        val = transform(subject_num, val)
    return val



card_loops = loopify(1, 7, INPUT_CARD)
print("Card loops: ", card_loops)
door_loops = loopify(1, 7, INPUT_DOOR)
print("Door loops: ", door_loops)

"""
Card loops:  14775052
Door loops:  12413864
"""

encryption_key_a = gen_encryption(1, INPUT_DOOR, card_loops)
print("Encryption Key A: ", encryption_key_a)
encryption_key_b = gen_encryption(1, INPUT_CARD, door_loops)
print("Encryption Key B: ", encryption_key_b)

