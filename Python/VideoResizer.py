from moviepy import VideoFileClip
#this was stolen from here: https://zulko.github.io/moviepy/reference/reference/moviepy.video.fx.Resize.html#module-moviepy.video.fx.Resize, it just redices the resolution of a video
def reduce_video_size(input_video_path, output_video_path, target_resolution):
    # Load the video file
    clip = VideoFileClip(input_video_path)

    # Reduce the resolution of the video
    reduced_clip = clip.resized(new_size=target_resolution)

    # Write the reduced video to the output file
    reduced_clip.write_videofile(output_video_path, codec='libx264', audio_codec='aac')

    # Close the clips to release resources
    clip.close()
    reduced_clip.close()

if __name__ == "__main__":
    # Input video path
    input_video = "BadAppleOriginal.mp4"

    # Output video path
    output_video = "BadAppleLR.mp4"

    # Target resolution (width, height)
    resolution = (12, 8)  # You can change this to your desired resolution

    # Reduce the size of the video
    reduce_video_size(input_video, output_video, resolution)

    print(f"Video size has been reduced and saved to {output_video}")