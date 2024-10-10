import psutil
import platform
import time
from datetime import datetime
import shutil
count = 0
countdown = 10
while 1 > 0:   
    #this coppies the minecraft logs
    sourceFile = "C:\\Users\Tecba\Desktop\Minecraft SMP\logs\latest.log"
    destinationFile = "C:\\xampp\htdocs hummasbeings\latest.log"
    shutil.copy2(sourceFile, destinationFile, follow_symlinks=True)
    print("copy done. Repeating in 10 seconds.")
    with open('file.txt', 'a') as f:
        def get_size(bytes, suffix="B"):
            """
            Scale bytes to its proper format
            e.g:
                1253656 => '1.20MB'
                1253656678 => '1.17GB'
            """
            factor = 1024
            for unit in ["", "K", "M", "G", "T", "P"]:
                if bytes < factor:
                    return f"{bytes:.2f}{unit}{suffix}"
                bytes /= factor
                
        print("="*40, "System Information", "="*40, file=f)
        uname = platform.uname()
        print(f"System: {uname.system}", file=f)
        print(f"Node Name: {uname.node}", file=f)
        print(f"Release: {uname.release}", file=f)
        print(f"Version: {uname.version}", file=f)
        print(f"Machine: {uname.machine}", file=f)
        print(f"Processor: {uname.processor}", file=f)

        # Boot Time
        print("="*40, "Time", "="*40, file=f)
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}", file=f)
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Current Time: ", dt_string, file=f) 
        
        # let's print CPU information
        print("="*40, "CPU Info", "="*40, file=f)
        # number of cores
        print("Physical cores:", psutil.cpu_count(logical=False), file=f)
        print("Total cores:", psutil.cpu_count(logical=True), file=f)
        # CPU frequencies
        cpufreq = psutil.cpu_freq()
        print(f"Max Frequency: {cpufreq.max:.2f}Mhz", file=f)
        print(f"Min Frequency: {cpufreq.min:.2f}Mhz", file=f)
        print(f"Current Frequency: {cpufreq.current:.2f}Mhz", file=f)
        # CPU usage
        print("CPU Usage Per Core:", file=f)
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            print(f"Core {i}: {percentage}%", file=f)
        print(f"Total CPU Usage: {psutil.cpu_percent(interval=1)}%", file=f)

        # Memory Information
        print("="*40, "Memory Information", "="*40, file=f)
        # get the memory details
        svmem = psutil.virtual_memory()
        print(f"Total: {get_size(svmem.total)}", file=f)
        print(f"Available: {get_size(svmem.available)}", file=f)
        print(f"Used: {get_size(svmem.used)}", file=f)
        print(f"Percentage: {svmem.percent}%", file=f)
        print("="*20, "SWAP", "="*20, file=f)
        # get the swap memory details (if exists)
        swap = psutil.swap_memory()
        print(f"Total: {get_size(swap.total)}", file=f)
        print(f"Free: {get_size(swap.free)}", file=f)
        print(f"Used: {get_size(swap.used)}", file=f)
        print(f"Percentage: {swap.percent}%", file=f)

        # Disk Information
        print("="*40, "Disk Information", "="*40, file=f)
        print("Partitions and Usage:", file=f)
        # get all disk partitions
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"=== Device: {partition.device} ===", file=f)
            print(f"  Mountpoint: {partition.mountpoint}", file=f)
            print(f"  File system type: {partition.fstype}", file=f)
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                # this can be catched due to the disk that
                # isn't ready
                continue
            print(f"  Total Size: {get_size(partition_usage.total)}", file=f)
            print(f"  Used: {get_size(partition_usage.used)}", file=f)
            print(f"  Free: {get_size(partition_usage.free)}", file=f)
            print(f"  Percentage: {partition_usage.percent}%", file=f)
        # get IO statistics since boot
        disk_io = psutil.disk_io_counters()
        print(f"Total read: {get_size(disk_io.read_bytes)}", file=f)
        print(f"Total write: {get_size(disk_io.write_bytes)}", file=f)

        # Network information
        print("="*40, "Network Information", "="*40, file=f)
        # get all network interfaces (virtual and physical)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"=== Interface: {interface_name} ===", file=f)
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  IP Address: {address.address}", file=f)
                    print(f"  Netmask: {address.netmask}", file=f)
                    print(f"  Broadcast IP: {address.broadcast}", file=f)
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address: {address.address}", file=f)
                    print(f"  Netmask: {address.netmask}", file=f)
                    print(f"  Broadcast MAC: {address.broadcast}", file=f)
        # get IO statistics since boot
        net_io = psutil.net_io_counters()
        print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}", file=f)
        print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}", file=f)
        
        #i wanted to see how many loops are do so thats this
        count = count + 1
        print(f"On loop Number: {count}", file=f)
        
        #tells us when program has run and how long left
        print("loop done. Repeating in 10 seconds.")
        
        #makes the program wait before restarting
        time.sleep(10)
        
        #clears file.txt at the end of the loop
        file = open("file.txt","r+")
        file.truncate(0)
        file.close()


