import cv2
import os

def extract_frames(video_folder, output_folder, save_every_nth_frame):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get all video files in the folder (you can specify extensions as needed)
    video_files = [os.path.join(video_folder, f) for f in os.listdir(video_folder) if f.endswith('.mp4')]

    # Iterate through each video file
    for video_path in video_files:
        video_name = os.path.basename(video_path)
        video_name_without_ext = os.path.splitext(video_name)[0]

        # Open the video file
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print(f"Error opening video file: {video_path}")
            continue

        frame_count = 0

        while True:
            # Read the next frame
            ret, frame = cap.read()
            if not ret:
                break  # Exit loop if no more frames are available

            # Save the frame if it's the nth frame
            if frame_count % save_every_nth_frame == 0:
                output_path = os.path.join(output_folder, f"{video_name_without_ext}_frame{frame_count}.png")
                cv2.imwrite(output_path, frame)
                print(f"Saved: {output_path}")

            frame_count += 1

        # Release the video capture object
        cap.release()

    print("Processing complete.")

if __name__ == "__main__":
    # Read configurations from environment variables
    video_folder = os.getenv('VIDEO_FOLDER', '/videos')
    output_folder = os.getenv('OUTPUT_FOLDER', '/output')
    save_every_nth_frame = int(os.getenv('SAVE_EVERY_NTH_FRAME', '1'))  # Default is 1, saving every frame

    # Call the function with parsed environment variables
    extract_frames(
        video_folder=video_folder,
        output_folder=output_folder,
        save_every_nth_frame=save_every_nth_frame
    )
