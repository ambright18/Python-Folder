#create a variable to hold our required temperature units
temperature_scales = {
    'Celsius': 'C',
    'Fahrenheit': 'F',
    'Kelvin': 'K'
}

#now, let's create a function that will hold the needed algorithms to convert temperatures.
def convert_temperature(value, input_scale, output_scale):
    if input_scale == 'C':
        if output_scale == 'F':
            return value * 1.8 + 32
        elif output_scale == 'K':
            return value + 273.15
        else: 
            return value
    elif input_scale == 'F':
        if output_scale == 'C':
            return (value - 32)/ 1.8
        elif output_scale == 'K':
            return (value + 459.67) * 5/9
        else:
            return value
    elif input_scale == 'K':
        if output_scale == 'C':
            return value - 273.15
        elif output_scale == 'F':
            return value * 9/5 - 459.67
        else: 
            return value
    else:
        return value
# end of function 

#There, the conversion function is complete, now let's create our prompts for the user

while True:
    print('Enter the input temperature value here: ')
    value = float(input())
    print("Enter the input temperature scale (C, F, K) here: ")
    input_scale = input().upper()
    print("Enter the output temperature you'd like to see converted (C, F, K) here: ")
    output_scale = input().upper()

    #convert and print result using our function
    result = convert_temperature(value, input_scale, output_scale)
    print(f'{value} {input_scale} = {result} {output_scale}')

    print("Enter 'q' to quit, or any other key to continue: ")
    choice = input()
    if choice.lower() == 'q':
        break        

