def caesar_cipher(text, shift):
    """Шифр Цезаря"""
    result = []
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(shifted.upper() if is_upper else shifted)
        else:
            result.append(char)
    return ''.join(result)

def process_encryption_chain(initial_text, commands):
    """Обработка цепочки команд шифрования"""
    steps = [initial_text]  
    current_text = initial_text
    
    for command in commands:
        try:
            if command.startswith('c'):
                shift = int(command[1:])
                current_text = caesar_cipher(current_text, shift)
                
            elif command == 'r':
                current_text = current_text[::-1]
                
            else:
                print(f"Неизвестная команда: {command}")
                continue
                
            steps.append(current_text)
            
        except Exception as e:
            print(f"Ошибка в команде '{command}': {e}")
            continue
    
    return current_text, steps


initial_text = "abcd"
commands = ["c1", "r", "c-1", "r"]

result, steps = process_encryption_chain(initial_text, commands)

print("Все этапы преобразования:")
for i, step in enumerate(steps):
    print(f"Шаг {i}: {step}")

print(f"\nИтоговый результат: {result}")