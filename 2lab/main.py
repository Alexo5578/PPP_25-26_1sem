

if __name__ == "__main__":
    def process_encryption_chain(original_string, commands):
    steps = [original_string]
    
    current_string = original_string
    
    for command in commands.split():
        try:
            if command.startswith('c'):
                shift = int(command[1:])
                current_string = caesar_cipher(current_string, shift)
                steps.append(current_string)
                
            elif command == 'r':
                current_string = current_string[::-1]
                steps.append(current_string)
                
            else:
                raise ValueError(f"Неизвестная команда: {command}")
                
        except Exception as e:
            print(f"Ошибка при обработке команды '{command}': {e}")
            continue
    
    return steps

def caesar_cipher(text, shift):
    result = []
    
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
        else:
            result.append(char)
    
    return ''.join(result)

if __name__ == "__main__":
    commands = "c1 r c-1 r"
    original_string = "abcd"
    
    steps = process_encryption_chain(original_string, commands)
    
    print("Все этапы преобразования:")
    for i, step in enumerate(steps):
        print(f"Шаг {i}: {step}")
    
    print(f"\nИсходная строка: {original_string}")
    print(f"Результат: {steps[-1]}")