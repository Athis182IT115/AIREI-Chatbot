import streamlit as st
# Set page title and icon
st.set_page_config(page_title='MyPalm', page_icon='sime_logo.png')

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

        if st.session_state.button6:
            st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
            st.markdown("<h6 style='text-align: right; color:black;'>Oil Losses</h6>", unsafe_allow_html=True)
            st.divider()
            st.image("sime_logo.png", width=25)
            #st.write("__**:white[Pick your Query below!!!]**__")
            button61 = st.button("__**:orange[What is the use of oil loss prediction and where to see?]**__", key='61')
            button62 = st.button("__**:orange[Why there is no prediction in the oil loss prediction page?]**__", key='62')
            button63 = st.button("__**:orange[How to get Oil Loss report?]**__", key='63')
            st.divider()
            st.chat_input("Pick your Query above!")
            if 'button61' not in st.session_state:
                st.session_state.button61 = False
            if 'button62' not in st.session_state:
                st.session_state.button62 = False
            if 'button63' not in st.session_state:
                st.session_state.button63 = False

            if button61:
                st.session_state.button61 = True
                st.session_state.button62 = False
                st.session_state.button63 = False
            if button62:
                st.session_state.button61 = False
                st.session_state.button62= True
                st.session_state.button63 = False
            if button63:
                st.session_state.button61 = False
                st.session_state.button62= False
                st.session_state.button63 = True

            if st.session_state.button61:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>What is the use of oil loss prediction and where to see?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[The 'Oil Loss Prediction' page is accessible on the mobile application for Supervisors, Engineers, and Management, while on the web application, it's available for Engineers and Management. This page aids in predicting oil losses using the hourly sterilizer and press data entered by users. It provides a list of potential reasons for oil losses and suggests actions to prevent them. Real-time oil loss prediction analysis helps palm oil mills make quicker decisions, enhance efficiency, and save money.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button62:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>Why there is no prediction in the oil loss prediction page?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[The hourly press and sterilizer data are important for oil loss prediction, user should make sure to enter the press and sterilizer data in a timely manner for the AI prediction to function effectively.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button63:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>How to get Oil Loss report?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[In the web application, you can find the 'Oil Loss' Report in the 'Production Reports' section through the dropdown menu. This report is accessible to Engineers and Management only.]**__")
                st.write("__**:white[In the mobile application, the 'Oil Loss' Report can be viewed under the 'Reports' menu by lab assistant, Engineers, Supervisors and Management.]**__")
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
                st.write("__**:white[This access is given to the Supervisor only. Supervisor can turn off a machinery via mobile application. In mobile application, go to the Dashboard and tap on the machine name. For Problem, select 'Not in Use/Shutdown']**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
    if st.session_state.button2:
        pass

    if st.session_state.button3:
        st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: right; color:black;'>General Questions</h6>", unsafe_allow_html=True)
        st.divider()
        st.image("sime_logo.png", width=25)
        #st.write("__**:white[Choose your domian below!!!]**__")
        button31 = st.button('__**:orange[System Functionality]**__', key='31')
        button32= st.button("__**:orange[User Query]**__", key='32')
        button33= st.button("__**:orange[QR code]**__", key='33')

        st.divider()
        st.chat_input("Select your Category above!")
        if 'button31' not in st.session_state:
            st.session_state.button31 = False
        if 'button32' not in st.session_state:
            st.session_state.button32 = False
        if 'button33' not in st.session_state:
            st.session_state.button33 = False


        if button31:
            st.session_state.button31 = True
            st.session_state.button32 = False
            st.session_state.button33 = False
        if button32:
            st.session_state.button31 = False
            st.session_state.button32 = True
            st.session_state.button33 = False
        if button33:
            st.session_state.button31 = False
            st.session_state.button32= False
            st.session_state.button33= True

        if st.session_state.button31:
            st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
            st.markdown("<h6 style='text-align: right; color:black;'>System Functionality</h6>", unsafe_allow_html=True)
            st.divider()
            st.image("sime_logo.png", width=25)
            #st.write("__**:white[Pick your Query below!!!]**__")
            button311 = st.button("__**:orange[How to add new user?]**__", key='311')
            button312 = st.button("__**:orange[How to add new station?]**__", key='312')
            button313 = st.button("__**:orange[How to access and view Weekly Report in web application?]**__", key='313')
            button314 = st.button("__**:orange[Can MyPalm keep records of previous mill data?]**__", key='314')
            button315 = st.button("__**:orange[Why does the screen display 'Unable to connect to the server,' and I cannot enter any data?]**__", key="315")
            button316 = st.button("__**:orange[Why is the Page stuck or continuously loading, and I couldn't view any records?]**__", key='316')
            st.divider()
            st.chat_input("Pick your Query above!")
            if 'button311' not in st.session_state:
                st.session_state.button311 = False
            if 'button312' not in st.session_state:
                st.session_state.button312 = False
            if 'button313' not in st.session_state:
                st.session_state.button313 = False
            if 'button314' not in st.session_state:
                st.session_state.button314 = False
            if 'button315' not in st.session_state:
                st.session_state.button315 = False
            if 'button316' not in st.session_state:
                st.session_state.button316 = False

            if button311:
                st.session_state.button311 = True
                st.session_state.button312 = False
                st.session_state.button313 = False
                st.session_state.button314= False
                st.session_state.button315=False
                st.session_state.button316=False
            if button312:
                st.session_state.button311 = False
                st.session_state.button312 = True
                st.session_state.button313 = False
                st.session_state.button314= False
                st.session_state.button315=False
                st.session_state.button316=False
            if button313:
                st.session_state.button311 = False
                st.session_state.button312 = False
                st.session_state.button313 = True
                st.session_state.button314= False
                st.session_state.button315=False
                st.session_state.button316=False
            if button314:
                st.session_state.button311 = False
                st.session_state.button312 = False
                st.session_state.button313 = False
                st.session_state.button314= True
                st.session_state.button315=False
                st.session_state.button316=False
            if button315:
                st.session_state.button311 = False
                st.session_state.button312 = False
                st.session_state.button313 = False
                st.session_state.button314= False
                st.session_state.button315=True
                st.session_state.button316=False
            if button316:
                st.session_state.button311 = False
                st.session_state.button312 = False
                st.session_state.button313 = False
                st.session_state.button314= False
                st.session_state.button315=False
                st.session_state.button316=True

            if st.session_state.button311:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>How to add new user?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[Please contact the Engineer to add a new user using the web application.]**__")
                st.write("__**:white[The Engineer can follow these steps :]**__")
                st.write("__**:white[1. Go to 'User Master'.]**__")
                st.write("__**:white[2. Click on 'Add New User'.]**__")
                st.write("__**:white[3. Enter the User's name.]**__")
                st.write("__**:white[4. Select the User Category.]**__")
                st.write("__**:white[5. Enter the username and password.]**__")
                st.write("__**:white[6. Click 'Save'.]**__")
                st.write("__**:white[A new login will be created for the user. Please provide the username and password to the user so they can log in.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button312:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>How to add new station?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[Please contact the Engineer to add a new station using the web application.]**__")
                st.write("__**:white[The Engineer can follow these steps :]**__")
                st.write("__**:white[1. Go to 'Station Master'.]**__")
                st.write("__**:white[2. Click on 'Add New Station'.]**__")
                st.write("__**:white[3. Enter the Station's name.]**__")
                st.write("__**:white[4. There is no need to change the Station's code.]**__")
                st.write("__**:white[5. Select the option whether to display the added station on the Maintenance Dashboard ]**__")
                st.write("__**:white[6. Click 'Save.']**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button313:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>How to access and view Weekly Report in web application?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[The weekly report is accessible to both Engineers and Management through the web application. To view it, go to the 'Weekly Report' tab and use the date filter to access the report as needed.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button314:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>Can MyPalm keep records of previous mill data?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[Yes, MyPalm maintains records of all data entered into it. Its user-friendly interface allows easy search, retrieval and access to records as needed.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button315:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>Why does the screen display 'Unable to connect to the server,' and I cannot enter any data?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[We are currently making some changes, and MyPalm will be accessible soon. Please try again later or please contact us via WhatsApp.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button316:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>Why is the Page stuck or continuously loading, and I couldn't view any records?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[Please close the app and clear it from running in the background on your phone. Then, try accessing the app again. If you encounter the same problem, please contact us via WhatsApp.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")

        if st.session_state.button32:
            st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
            st.markdown("<h6 style='text-align: right; color:black;'>User Query</h6>", unsafe_allow_html=True)
            st.divider()
            st.image("sime_logo.png", width=25)
            #st.write("__**:white[Pick your Query below!!!]**__")
            button321 = st.button("__**:orange[What Engineer can do and view in MyPalm?]**__", key='321')
            button322 = st.button("__**:orange[What Foreman & Chargeman can do and view in MyPalm?]**__", key='322')
            button323 = st.button("__**:orange[What Supervisor can do and view in MyPalm?]**__", key='323')
            button324 = st.button("__**:orange[I have forgotten my ID and password]**__", key='324')
            button325 = st.button("__**:orange[What if there is no operator to key in the data?]**__", key="325")
            button326 = st.button("__**:orange[I need to add worker's name in the work assign list]**__", key='326')
            st.divider()
            st.chat_input("Pick your Query above!")
            if 'button321' not in st.session_state:
                st.session_state.button321 = False
            if 'button322' not in st.session_state:
                st.session_state.button322 = False
            if 'button323' not in st.session_state:
                st.session_state.button323 = False
            if 'button324' not in st.session_state:
                st.session_state.button324 = False
            if 'button325' not in st.session_state:
                st.session_state.button325 = False
            if 'button326' not in st.session_state:
                st.session_state.button326 = False

            if button321:
                st.session_state.button321 = True
                st.session_state.button322 = False
                st.session_state.button323 = False
                st.session_state.button324= False
                st.session_state.button325=False
                st.session_state.button326=False
            if button322:
                st.session_state.button321 = False
                st.session_state.button322 = True
                st.session_state.button323 = False
                st.session_state.button324= False
                st.session_state.button325=False
                st.session_state.button326=False
            if button323:
                st.session_state.button321 = False
                st.session_state.button322 = False
                st.session_state.button323 = True
                st.session_state.button324= False
                st.session_state.button325=False
                st.session_state.button326=False
            if button324:
                st.session_state.button321 = False
                st.session_state.button322 = False
                st.session_state.button323 = False
                st.session_state.button324= True
                st.session_state.button325=False
                st.session_state.button326=False
            if button325:
                st.session_state.button321 = False
                st.session_state.button322 = False
                st.session_state.button323 = False
                st.session_state.button324= False
                st.session_state.button325=True
                st.session_state.button326=False
            if button326:
                st.session_state.button321 = False
                st.session_state.button322 = False
                st.session_state.button323 = False
                st.session_state.button324= False
                st.session_state.button325=False
                st.session_state.button326=True

            if st.session_state.button321:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>What Engineer can do and view in MyPalm?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[Below are the list of task and responsibilities of an Engineer in MyPalm system ]**__")
                st.write("__**:white[1. Create Corrective Maintenance notification ]**__")
                st.write("__**:white[2. Do acknowledgement for Corrective Maintenance and Preventive Maintenance records ]**__")
                st.write("__**:white[3. Master data update:user list, station list, machinery list with parts details (with Routine Preventive Maintenance schedule & Replacement Preventive Maintenance maximum running hours settings).]**__")
                st.write("__**:white[4. View production and maintenance reports via both mobile and web application.]**__")
                st.write("__**:white[5. Generate QR code for machinery.]**__")
                st.write("__**:white[6. Do acknowledgement for production alerts attended by Supervisors.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button322:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>What Foreman & Chargeman can do and view in MyPalm?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[Below are the list of task and responsibilities of a Foreman & Chargeman in MyPalm system]**__")
                st.write("__**:white[1. Create Corrective Maintenance notification]**__")
                st.write("__**:white[2. Update Corrective Maintenance notification reported by Engineer and Supervisor.]**__")
                st.write("__**:white[3. Assign Corrective Maintenance and Preventive Maintenance records to fitter and chargeman]**__")
                st.write("__**:white[4. Do verification for Corrective Maintenance and Preventive Maintenance records ]**__")
                st.write("__**:white[5. View Maintenance reports via mobile application]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button323:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>What Supervisor can do and view in MyPalm?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[Below are the list of task and responsibilities of a Supervisor in MyPalm system]**__")
                st.write("__**:white[1. Start-stop production & machineries]**__")
                st.write("__**:white[2. Turn on and off stations.]**__")
                st.write("__**:white[3. Report mill breakdown]**__")
                st.write("__**:white[4. Create Corrective Maintenance notification]**__")
                st.write("__**:white[5. View Maintenance Report]**__")
                st.write("__**:white[6. View Production Report]**__")
                st.write("__**:white[7. Attend Production alerts]**__")
                st.write("__**:white[8. Update FFB cages]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button324:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>I have forgotten my ID and password]</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[Please contact us via WhatsApp and provide your name and mill code.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button325:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>What if there is no operator to key in the data?</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[If there is no designated operator available to input the data, please contact us via WhatsApp to inform us or to request a backup ID.]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
            if st.session_state.button326:
                st.markdown("<p align='right'> <img width='28' src='https://cdn-icons-png.flaticon.com/128/1256/1256650.png'> </p>", unsafe_allow_html=True)
                st.markdown("<h6 style='text-align: right; color:black;'>I need to add worker's name in the work assign list</h6>", unsafe_allow_html=True)
                st.divider()
                st.image("sime_logo.png", width=25)
                st.write("__**:white[Please contact Engineer to add the worker's name as a Fitter user in the web application under User Master screen and you will be able to see the added worker's name in the assign list. ]**__")
                st.divider()
                st.chat_input("Thank You for using MyPalm Bot!!")
