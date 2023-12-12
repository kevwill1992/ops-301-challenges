# Script Name:                    Psutil
# Author:                         Kevin Williams
# Date of Lastest revision:       12/11/2023
# Purpose:                        Using psutil to fetch system information
# Additional Sources:             https://chat.openai.com/share/20203eda-013c-44c3-991d-4fffc6e6c881

import psutil

def get_cpu_times():
    # Get CPU times
    cpu_times = psutil.cpu_times()

    # Extract individual CPU time components
    user_mode_time = cpu_times.user
    kernel_mode_time = cpu_times.system
    idle_time = cpu_times.idle
    priority_user_mode_time = cpu_times.nice
    io_wait_time = cpu_times.iowait
    hardware_interrupt_time = cpu_times.irq
    software_interrupt_time = cpu_times.softirq
    virtualized_os_time = cpu_times.steal
    virtual_cpu_time = cpu_times.guest

    # Print the obtained CPU times
    print(f"Time spent by normal processes executing in user mode: {user_mode_time} seconds")
    print(f"Time spent by processes executing in kernel mode: {kernel_mode_time} seconds")
    print(f"Time when the system was idle: {idle_time} seconds")
    print(f"Time spent by priority processes executing in user mode: {priority_user_mode_time} seconds")
    print(f"Time spent waiting for I/O to complete: {io_wait_time} seconds")
    print(f"Time spent for servicing hardware interrupts: {hardware_interrupt_time} seconds")
    print(f"Time spent for servicing software interrupts: {software_interrupt_time} seconds")
    print(f"Time spent by other operating systems running in a virtualized environment: {virtualized_os_time} seconds")
    print(f"Time spent running a virtual CPU for guest operating systems: {virtual_cpu_time} seconds")

if __name__ == "__main__":
    # Call the function to get and print CPU times
    get_cpu_times()

# done