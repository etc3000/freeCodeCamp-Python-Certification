def hanoi_solver(sol_num):
    source_rod = list(range(sol_num, 0,-1))
    middle_rod = []
    target_rod = []

    output = ''

    def save_move():
        nonlocal output
        output += f'{source_rod} {middle_rod} {target_rod}\n'

    def move_disk(n, source_rod, middle_rod, target_rod):
        if n == 1:
            target_rod.append(source_rod.pop())
            save_move()
        else:
            move_disk(n - 1, source_rod, middle_rod, target_rod)
            target_rod.append(source_rod.pop())
            save_move()
            move_disks(n - 1, middle_rod, target_rod, source_rod)
        
    save_move()
    move_disk(sol_num, source_rod, target_rod, middle_rod)

    return output[:-1]
