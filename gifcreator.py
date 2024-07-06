import moviepy.editor as mp

# List of image file paths
image_files = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg"]

# Load images as clips
clips = [mp.ImageClip(img).set_duration(0.5) for img in image_files]

# Concatenate the clips into a single video
video = mp.concatenate_videoclips(clips, method="compose")

# Write the result to a GIF file
video.write_gif("output.gif", fps=3)

print("GIF created successfully and saved as 'output.gif'")
