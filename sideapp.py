import streamlit as st

# Set page title and icon
st.set_page_config(page_title='MyPalm', page_icon='sime_logo.png')

# Display your logo
st.image('mypalm_logo.png', width=220)
# Create buttons for different sections
st.image("sime_logo.png", width=25)
st.chat_input("Hi! I am MyPalm Bot!! Select language!")
button0 = st.button('__**:orange[English]**__',key='0')
button00 = st.button("__**:orange[Malay]**__",key='00')
if 'button0' not in st.session_state:
    st.session_state.button0 = False
if 'button00' not in st.session_state:
    st.session_state.button00 = False

if button0:
    st.session_state.button0 = True
    st.session_state.button00 = False
if button00:
    st.session_state.button0 = False
    st.session_state.button00 = True

if st.session_state.button0:
    st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: right; color:black;'>English</h6>", unsafe_allow_html=True)
    st.divider()
    st.image("sime_logo.png", width=25)
    button1 = st.button('__**:orange[Production Module]**__', key='1')
    button2 = st.button("__**:orange[Maintenance Module]**__", key='2')
    button3 = st.button("__**:orange[General Questions]**__", key='3')
    st.divider()
    st.chat_input("Pick your domain!")
    # Initialize session_state
    if 'button1' not in st.session_state:
        st.session_state.button1 = False
    if 'button2' not in st.session_state:
        st.session_state.button2 = False
    if 'button3' not in st.session_state:
        st.session_state.button3 = False


    # Handle button clicks
    if button1:
        st.session_state.button1 = True
        st.session_state.button2 = False
        st.session_state.button3 = False

    if button2:
        st.session_state.button1 = False
        st.session_state.button2 = True
        st.session_state.button3 = False

    if button3:
        st.session_state.button1 = False
        st.session_state.button2 = False
        st.session_state.button3 = True
     

    # Display content based on button clicks
    if st.session_state.button1:
        st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: right; color:black;'>Production Module</h6>", unsafe_allow_html=True)
        st.divider()
        st.image("sime_logo.png", width=25)
        #st.write("__**:white[Choose your domian below!!!]**__")
        button4 = st.button('__**:orange[Sterilization]**__', key='4')
        button5 = st.button("__**:orange[Pressing ]**__", key='5')
        button6 = st.button("__**:orange[Oil Losses]**__", key='6')
        button7 = st.button("__**:orange[Mill Production and Breakdown]**__", key='7')
        st.divider()
        st.chat_input("Select your Working Station above!")
        if 'button4' not in st.session_state:
            st.session_state.button4 = False
        if 'button5' not in st.session_state:
            st.session_state.button5 = False
        if 'button6' not in st.session_state:
            st.session_state.button6 = False
        if 'button7' not in st.session_state:
            st.session_state.button7 = False

        if button4:
            st.session_state.button4 = True
            st.session_state.button5 = False
            st.session_state.button6 = False
            st.session_state.button7 = False
        if button5:
            st.session_state.button4 = False
            st.session_state.button5 = True
            st.session_state.button6 = False
            st.session_state.button7 = False
        if button6:
            st.session_state.button4 = False
            st.session_state.button5 = False
            st.session_state.button6 = True
            st.session_state.button7 = False
        if button7:
            st.session_state.button4 = False
            st.session_state.button5 = False
            st.session_state.button6 = False
            st.session_state.button7 = True

        if st.session_state.button4:
            st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
            st.markdown("<h6 style='text-align: right; color:black;'>Sterilization</h6>", unsafe_allow_html=True)
            st.divider()
            st.image("sime_logo.png", width=25)
            #st.write("__**:white[Pick your Query below!!!]**__")
            button41 = st.button("__**:orange[Why can't I key in sterilizer data?]**__", key='41')
            button42 = st.button("__**:orange[What should I do if I entered date incorrectly?]**__", key='42')
            button43 = st.button("__**:orange[How do I key in if there is no peak graph?]**__", key='43')
            button44 = st.button("__**:orange[How to get Sterilization Station report?]**__", key='44')
            st.divider()
            st.chat_input("Pick your Query above!")
            if 'button41' not in st.session_state:
                st.session_state.button41 = False
            if 'button42' not in st.session_state:
                st.session_state.button42 = False
            if 'button43' not in st.session_state:
                st.session_state.button43 = False
            if 'button44' not in st.session_state:
                st.session_state.button44 = False

            if button41:
                st.session_state.button41 = True
                st.session_state.button42 = False
                st.session_state.button43 = False
                st.session_state.button44 = False
            if button42:
                st.session_state.button41 = False
                st.session_state.button42= True
                st.session_state.button43 = False
                st.session_state.button44 = False
            if button43:
                st.session_state.button41 = False
                st.session_state.button42= False
                st.session_state.button43 = True
                st.session_state.button44 = False
            if button44:
                st.session_state.button41 = False
                st.session_state.button42 = False
                st.session_state.button43 = False
                st.session_state.button44 = True

            if st.session_state.button41:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>Why can't I key in sterilizer data?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[If you are cannot enter the sterilizer data, it may be due to incorrect door shut and open times that were entered.]**__")
                st.write("__**:white[To address this issues you can follow this steps:]**__")
                st.write("__**:white[1. Check previous cycle door shut time & date.]**__")
                st.write("__**:white[2. If the previous cycle has been key in wrongly, please contact us via WhatsApp and send us the correct details so that we can assist in correcting the data.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button42:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>What should I do if I entered date incorrectly?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[You cannot change the date by yourself. Please contact us via WhatsApp and send us the correct details so that we can assist in correcting the data.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button43:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>How do I key in if there is no peak graph?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[If there is no graph generated for input, you may choose not to enter the cycle data. Please contact us via WhatsApp to inform this issues.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button44:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>How to get Sterilization Station report?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[In the web application, you can find the 'Sterilization Station' Report in the 'Production Reports' section through the dropdown menu. This report is accessible to Engineers and Management only.]**__")
                st.write("__**:white[In the mobile application, the 'Sterilization Station' Report can be viewed under the 'Reports' menu by sterilizer operators, Engineers, Supervisors and Management.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")

        if st.session_state.button5:
            st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
            st.markdown("<h6 style='text-align: right; color:black;'>Pressing</h6>", unsafe_allow_html=True)
            st.divider()
            st.image("sime_logo.png", width=25)
            #st.write("__**:white[Pick your Query below!!!]**__")
            button51 = st.button("__**:orange[Why am I getting too many notifications all at once?]**__", key='51')
            button52 = st.button("__**:orange[Why are the digestor and press offline, and why can't I enter data?]**__", key='52')
            button53 = st.button("__**:orange[How to get Pressing Station report?]**__", key='53')
            st.divider()
            st.chat_input("Pick your Query above!")
            if 'button51' not in st.session_state:
                st.session_state.button51 = False
            if 'button52' not in st.session_state:
                st.session_state.button52 = False
            if 'button53' not in st.session_state:
                st.session_state.button53 = False

            if button51:
                st.session_state.button51 = True
                st.session_state.button52 = False
                st.session_state.button53 = False
            if button52:
                st.session_state.button51 = False
                st.session_state.button52= True
                st.session_state.button53 = False
            if button53:
                st.session_state.button51 = False
                st.session_state.button52= False
                st.session_state.button53 = True

            if st.session_state.button51:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>Why am I getting too many notifications all at once?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[The notification is generated based on the door open time and date data entered by the sterilizer operator. If sterilizer cycles are happening frequently, you'll get more notifications.]**__")
                st.write("__**:white[If you receive the same notification multiple times within a 15-minutes, you can choose either to key in the data or skip it.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button52:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>Why are the digestor and press offline, and why can't I enter data?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[If the digester and press are offline, it could be due to:]**__")
                st.write("__**:white[1. The machinery being turned off]**__")
                st.write("__**:white[2. The machinery undergoing a breakdown]**__")
                st.write("__**:white[To address these issues, please inform the foreman and supervisor to turn it back on.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button53:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>How to get Pressing Station report?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[In the web application, you can find the 'Pressing Station' Report in the 'Production Reports' section through the dropdown menu. This report is accessible to Engineers and Management only.]**__")
                st.write("__**:white[In the mobile application, the 'Pressing Station' Report can be viewed under the 'Reports' menu by Press Operators, Engineers, Supervisors and Management.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")

        if st.session_state.button7:
            st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
            st.markdown("<h6 style='text-align: right; color:black;'>Mill Production and Breakdown</h6>", unsafe_allow_html=True)
            st.divider()
            st.image("sime_logo.png", width=25)
            #st.write("__**:white[Pick your Query below!!!]**__")
            button8 = st.button('__**:orange[How to Start the Production?]**__', key='8')
            button9 = st.button("__**:orange[How to Stop the Production?]**__", key='9')
            button10 = st.button("__**:orange[How to turn On the machine?]**__", key='10')
            button11 = st.button("__**:orange[How to turn Off the machine?]**__", key='11')
            st.divider()
            st.chat_input("Pick your Query above!")
            if 'button8' not in st.session_state:
                st.session_state.button8 = False
            if 'button9' not in st.session_state:
                st.session_state.button9 = False
            if 'button10' not in st.session_state:
                st.session_state.button10 = False
            if 'button11' not in st.session_state:
                st.session_state.button11 = False

            if button8:
                st.session_state.button8 = True
                st.session_state.button9 = False
                st.session_state.button10 = False
                st.session_state.button11 = False
            if button9:
                st.session_state.button8 = False
                st.session_state.button9 = True
                st.session_state.button10 = False
                st.session_state.button11 = False
            if button10:
                st.session_state.button8 = False
                st.session_state.button9 = False
                st.session_state.button10 = True
                st.session_state.button11 = False
            if button11:
                st.session_state.button8 = False
                st.session_state.button9 = False
                st.session_state.button10 = False
                st.session_state.button11 = True

            if st.session_state.button8:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>How to Start the Production?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[This access is given to the Supervisor only. Supervisor can start the mill production via mobile application. In mobile application, go to the Dashboard and tap on the 'Start Production' button.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button9:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>How to Stop the Production?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[This access is given to the Supervisor only. Supervisor can stop the mill production via mobile application. In mobile application, go to the Dashboard and tap on the 'Stop Production' button.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button10:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>How to turn On the machine?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[This access is given to the Supervisor only. Supervisor can turn on a machinery via mobile application. In mobile application, go to the Dashboard and tap on the machine name which has been turned off. Give Yes to the option 'Turn on the machine']**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button11:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>How to turn Off the machine?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[This access is given to the Supervisor only. Supervisor can turn off a machinery via mobile application. In mobile application, go to the Dashboard and tap on the machine name. For Problem, select 'Not in Use/Sutdown']**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
    if st.session_state.button2:
        st.write("button2 is True")

        if st.button('Check 2'):
            st.write("Do your logic here")

    if st.session_state.button3:
        st.write("button3 is True")

        if st.button('Check 3'):
            st.write("Do your logic here")
