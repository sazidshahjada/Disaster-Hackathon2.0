import cv2
import os

def extract_frames(video_path, output_folder, interval):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * interval)
    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if ret:
            if frame_count % frame_interval == 0:
                frame_filename = os.path.join(output_folder, f'frame_{saved_count:04d}.jpg')
                cv2.imwrite(frame_filename, frame)
                saved_count += 1
            frame_count += 1
        else:
            break

    cap.release()
    print(f"Extracted {saved_count} frames.")

if __name__ == "__main__":
    video_path = "/home/sajid/Work/DISASTER-HACKATHON-2.0/Videos/jamalpur.mp4"
    output_folder = 'output_frames'
    interval = 1
    extract_frames(video_path, output_folder, interval)
