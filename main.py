import time
from pypresence import Presence
import pygetwindow as gw

CLIENT_ID = 'CLIENT_ID'  # Discord AppID
RPC = Presence(CLIENT_ID)
RPC.connect()

running = True

start_time = None
elapsed_time = 0

while running:
    try:
        windows = gw.getWindowsWithTitle("FL Studio 2024")
        if windows:
            window = windows[0]
            project_name = window.title
            project_name = project_name.replace(" - FL Studio 2024", "")

            if start_time is None:
                start_time = time.time()

            elapsed_time = int(time.time() - start_time)

            RPC.update(
                state=f"Editing: {project_name}",
                details="Working in FL Studio",
                large_image="flstudio_logo",  # FL Studio Logo (u need to add it to your app !!)
                start=start_time,  
            )
        else:
            RPC.clear()
            start_time = None

        time.sleep(1)

    except KeyboardInterrupt:
        print("Programa interrumpido por el usuario.")
        running = False  
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5) 
