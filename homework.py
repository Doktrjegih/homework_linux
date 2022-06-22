import subprocess

as_string = subprocess.check_output(['ps', 'aux']).decode().splitlines()[1:]

users = []
for i in as_string:
    users.append(i.split()[0])
user_list = list(set(users))

user_processes = dict.fromkeys(user_list, 0)
for user in user_list:
    for i in as_string:
        if i.split()[0] == user:
            current_value = user_processes.get(f'{user}')
            user_processes.update({user: (int(current_value) + 1)})

mem = 0
for i in as_string:
    mem += int(i.split()[5])

cpu = 0.0
for i in as_string:
    cpu += float(i.split()[2])

all_mem = []
max_mem_name = ''
for i in as_string:
    all_mem.append(int(i.split()[5]))
max_mem = max(all_mem)
for j in as_string:
    if int(j.split()[5]) == max_mem:
        max_mem_name = j.split()[10]

all_cpu = []
max_cpu_name = ''
for i in as_string:
    all_cpu.append(float(i.split()[2]))
max_cpu = max(all_cpu)
for j in as_string:
    if float(j.split()[2]) == max_cpu:
        max_cpu_name = j.split()[10]

print('Отчет о состоянии системы:')
print(f'Пользователи системы: {user_list}')
print(f'Процессов запущено: {len(as_string)}')
print('Пользовательских процессов:')
for ps in user_processes:
    print(f'{ps}: {user_processes[ps]}')
print(f'Всего памяти используется: {round(mem / 1000, 2)} mb')
print(f'Всего CPU используется: {round(cpu, 1)}%')
print(f'Больше всего памяти использует: {max_mem_name[:20]}')
print(f'Больше всего CPU использует: {max_cpu_name[:20]}')
