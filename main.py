original_text=input("введите сообщение: ")
print(original_text)
length_text=len(original_text)
print(length_text)
print(original_text[1])
print(original_text[-1])
print(original_text[0:3])
print(original_text[-3:])
print(f"\u001b[31;1m{original_text}\u001b[0m")
color_start=int(input("с какого индекса хотите начать покраску: "))
color_end=int(input("на каком индексе хотите завершить покраску: "))
color_name=input("введите цвет для покраски(синий, красный,зеленый): ")
if color_name=="синий":
    colorized_text=f"{original_text[0:color_start]}\u001b[34m{original_text[color_start:color_end]}\u001b[0m{original_text[color_end:]}"
elif color_name=="зеленый": 
    colorized_text=f"{original_text[0:color_start]}\u001b[32m{original_text[color_start:color_end]}\u001b[0m{original_text[color_end:]}"
elif color_name=="красный": 
    colorized_text=f"{original_text[0:color_start]}\u001b[31m{original_text[color_start:color_end]}\u001b[0m{original_text[color_end:]}"
else:
    print("я не понимаю что вы выбрали, поэтому будет красный цвет по умалчанию")
    colorized_text=f"{original_text[0:color_start]}\u001b[31m{original_text[color_start:color_end]}\u001b[0m{original_text[color_end:]}"
print(colorized_text)
old_char=input("введите символ, который хотите заменить: ")
new_char=input("введите символ, на который хотите заменить: ")
modified_text=original_text.replace(old_char,new_char)
print(modified_text)
even_chars=modified_text[::2]
print(even_chars)
odd_chars=modified_text[1::2]
print(odd_chars)
reversed_text=original_text[::-1]
print(reversed_text)
middle_index = len(original_text)//2
swapped_text = original_text[middle_index:] + original_text[:middle_index]
print(swapped_text)