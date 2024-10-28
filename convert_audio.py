import ffmpeg

input_file = 'input.ogg'

output_file = 'output.wav'

ffmpeg.input(input_file).output(output_file).run()