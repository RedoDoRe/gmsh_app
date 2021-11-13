
dark_theme = '''
	/*QToolTip*/
	QToolTip {
		background-color: rgb(33, 33, 33);
        color: white; 
        font-size: 16px;
        border: 1px solid rgb(76, 162, 249);

	}

	/*QFrame*/

	QFrame#frame_menu_left,#frame_title_app,#frame_logo,#frame_footer,#frame_4,#frame_top
	{
		background-color:rgb(33, 33, 33);
		border:none;
		
	}
	QFrame#frame_header,#frame_btn_window,#frame_title_bottom,#frame_top,#frame_title
	{
		border:None;
	}

	QFrame#frame_body ,#frame_title_bottom
	{
		background-color:rgb(41, 45, 56);	
	}
	QLabel#label_timer_6,#label_timer_4
	{
		background-position: center;
		background-image: url(:/resource/iconapp/24x24/cil-arrow-circle-right.png);
		background-repeat:None;
	}
	
	/*QLineEdit*/
	QLineEdit
	{
		background-color:rgb(32, 33, 36);
		color: rgb(188, 192, 195);
		border:2px solid  rgb(65, 67, 71);
		border-radius: 5px;

	}

	QLineEdit:hover
	{	
		border:2px solid rgb(91, 93, 99);
	}
	QLineEdit:focus
	{	
		border: 2px solid rgb(91, 152, 248);
		color: rgb(188, 192, 195);	
	}
	/*QPushButton*/

	QPushButton#pushButton_home, #pushButton_get_cmt, #pushButton_setting, #pushButton_zoom_in, #pushButton_zoom_out, #pushButton_close
	{
		background-color:rgb(33, 33, 33);
		color: rgba(255,255,255,210);
		border: None;
		border-radius: None;

	}

	QPushButton#pushButton_home:hover, #pushButton_get_cmt:hover, #pushButton_setting:hover, #pushButton_zoom_in:hover, #pushButton_zoom_out:hover, #pushButton_close:hover
	{	
		background-color:rgb(65, 91, 116);
	}
	QPushButton#pushButton_home:pressed, #pushButton_get_cmt:pressed, #pushButton_setting:pressed, #pushButton_zoom_in:pressed, #pushButton_zoom_out:pressed, #pushButton_close:pressed
	{	
		background-color:rgb(96, 134, 171);
	}

	QPushButton
	{
		background-color:rgb(75, 104, 133);
		color: rgba(255,255,255,210);
		border: None;
		border-radius: 5px;
		background-repeat: None;
		background-position:center;

	}


	QPushButton:hover
	{	
		background-color:rgb(65, 91, 116);
		border: 2px solid rgb(91, 152, 248);	
	}
	QPushButton:pressed
	{	
		background-color:  rgb(96, 134, 171);
	}
	QPushButton#pushButton_home 
	{
	background-image: url(:/resource/iconapp/24x24/cil-sun.png);
	}
	QPushButton#pushButton_resize{
	background-image: url(:/16x16/iconapp/16x16/cil-size-grip.png);
	background-color:rgb(33, 33, 33);
	background-repeat:none;
	border-radius:-10px;
	}
	QPushButton#pushButton_resize:hover{
	border: none;
	}
	QPushButton#pushButton_zoom_in 
	{
	background-image: url(:/16x16/iconapp/16x16/cil-window-minimize.png);
	}
	QPushButton#pushButton_zoom_out
	{
	background-image: url(:/16x16/iconapp/16x16/cil-window-maximize.png);
	}
	QPushButton#pushButton_close
	{
	background-image: url(:/16x16/iconapp/16x16/cil-x.png);
	}
	QPushButton#pushButton_close:hover
	{
	background-color: rgb(255, 71, 35);
	}
	QPushButton#pushButton_close:pressed
	{
	background-color: rgb(252, 96, 66);
	}
	/*QSpinBox*/

	/*QGroupBox*/
	QGroupBox {
		color: rgb(255,255,255);
		border-radius: 5px;
		border: 1px solid rgb(91, 152, 248);	

	}
	/*QComboBox*/
	QComboBox,QSpinBox{
	color:rgb(255, 255, 255);
	background-color: rgb(75, 104, 133);
	border-radius: 5px;
	border: 1px solid rgb(48, 49, 52);
	padding-left:8px;
	}
	QComboBox::hover {
	background-color:rgb(65, 91, 116);
	border-color:rgb(96, 134, 171);
	}

	QComboBox::drop-down {
	    width: 30px;	
		background-image: url(:/16x16/iconapp/16x16/cil-arrow-bottom.png);
		background-repeat: None;
		background-position: center;

	}
	QComboBox QAbstractItemView
	{    
	    color: rgb(255, 255, 255);
		background-color:rgb(75, 104, 133);
	    selection-background-color: rgb(119, 155, 213);
		padding-left: 0px;
	}
	/*QSpinBox*/

	/*QLabel*/
	QLabel
	{
		color:rgb(188, 192, 195)
	}
	/*QTextEdit*/
	QTextEdit {	
		color: rgb(188, 192, 195);
		border-radius: 5px;
		border: 1px solid rgb(91, 152, 248);	
		background-color: rgb(32, 33, 36);
		padding-left:5px;
	}
	/* QCheckbox*/
	QCheckBox{
		color:rgb(188, 192, 195)

	}
	QCheckBox::indicator{
		color:rgb(255, 255, 255);
		border: 2px solid rgb(255,255,255);
		height: 20px;
		width:20px;
		border-radius:12px;
		background: rgb(44, 49, 60);
		
	}
	QCheckBox::indicator:hover{
		 border-radius: 10px;
	}
	QCheckBox::indicator:checked {
	 	background: 3px solid rgb(52, 59, 72);
	    border: 2px solid rgb(138, 180, 248);  
		border-radius:12px;     
		background-image: url(:/resource/iconapp/24x24/cil-check-alt.png);
		background-repeat:none;
	}

	QCheckBox#checkBox_num:indicator {
		width: 33px; 
		height: 23px;
		border-radius:-12px;
		border:1px solid rgb(255,255,255);

	}
	/* QRadioButton*/
	QRadioButton{
		color:rgb(188, 192, 195);

	}
	QRadioButton::indicator{
		color:rgb(188, 192, 195);
		border: 2px solid rgb(255,255,255);
		height: 20px;
		width:20px;
		border-radius:12px;
		background: rgb(44, 49, 60);
		
	}
	QRadioButton::indicator:hover{
		 border-radius: 10px;
	}
	QRadioButton::indicator:checked {
	 	background: 3px solid rgb(52, 59, 72);
	    border: 2px solid rgb(138, 180, 248);  
		border-radius:12px;     
		background-image: url(:/resource/iconapp/24x24/cil-check-alt.png);
	}

		/* SCROLL BARS*/
	QScrollBar:horizontal {
	    border: none;
	    background:rgb(39, 44, 54);
	    height: 8px;
	    margin: 0px 21px 0 21px;
		border-radius: 0px;
	}
	QScrollBar::handle:horizontal {
	    background: rgb(138, 180, 248);
	    min-width: 25px;
		border-radius: 3px
	}
	QScrollBar::add-line:horizontal {
	    border: none;
	    background:rgb(39, 44, 54);
		width: 20px;
		border-top-right-radius: 7px;
	    border-bottom-right-radius: 7px;
	    subcontrol-position: right;
	    subcontrol-origin: margin;
	}
	QScrollBar::sub-line:horizontal {
	    border: none;
	    background:rgb(39, 44, 54);
	    width: 20px;
		border-top-left-radius: 7px;
	    border-bottom-left-radius: 7px;
	    subcontrol-position: left;
	    subcontrol-origin: margin;
	}
	QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
	{
	     background: none;
	}
	QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
	{
	    background: none;
	}
	 QScrollBar:vertical {
		border: none;
	    background:rgb(39, 44, 54);
	    width: 8px;
	    margin: 10px 0px 0px 0px; /*top right*/
		border-radius: 0px;
	 }
	 QScrollBar::handle:vertical {	
		background:rgb(138, 180, 248);
	    min-height: 50px;
		border-radius: 3px
	 }
	 QScrollBar::add-line:vertical {
	    border: none;
	    background:rgb(39, 44, 54);
	    height: 20px;
		border-bottom-left-radius: 7px;
	    border-bottom-right-radius: 7px;
	    subcontrol-position: bottom;
	    subcontrol-origin: margin;
	 }
	 QScrollBar::sub-line:vertical {
		 border: none;
	     background:rgb(39, 44, 54);
	     height: 20px;
		 border-top-left-radius: 7px;
	     border-top-right-radius: 7px;
	     subcontrol-position: top;
	     subcontrol-origin: margin;
	 }
	 QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
	     background: none;
	 }

	 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
	     background: none;
	 }

	/*QtableWidget*/
	QTableWidget {	
	gridline-color: rgb(54, 73, 90);
	background-color: rgb(39, 44, 54);
	border-radius: 5px;
	border:None;
	color: rgb(230,230,230);
	}

	QTableWidget::item:selected{
	background-color: rgb(96, 134, 171);
	}

	QTableWidget::horizontalHeader {	
	background-color: rgb(33, 33, 33);
	}
	QHeaderView::section:horizontal
	{
	border: 1px solid rgb(54, 73, 90);
	background-color: rgb(33, 33, 33);
	color : rgb(188, 192, 195);

	}


	/*---------------------- Message Box ----------------------------*/
	
	QFrame#frame_msg_main {
	background-color:rgb(50, 50, 50);
	border: none;
	border-radius: 5px;
	}
	QFrame#frame_msg_header{
	background-color:qlineargradient(spread:reflect, x1:0, y1:0.136, x2:0, y2:1, stop:0 rgba(50, 50, 50, 255), stop:0.774011 rgba(81, 81, 81, 255));
	border-bottom: 1px solid rgb(34,34,34);
	border-radius: 5px;
	border-bottom-right-radius: -5px;
	border-bottom-left-radius: -5px;
	}
	/*QPushButton*/

	/*QPushButton ok */
	QPushButton#pushButton_ok {
	    color: rgb(255, 255, 255);
	    background-color: qlineargradient(spread:pad, x1:0, y1:0.994, x2:0, y2:0.0569545, stop:0.0340909 rgba(0, 170, 255, 255), stop:1 rgba(170, 214, 255, 255));
	    border: 1px solid rgb(76, 162, 249);
	    border-radius: 5px;
	       
	}
	QPushButton#pushButton_ok:hover { 
	    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 170, 255, 255), stop:0.755682 rgba(171, 224, 255, 255));
	    border: 2px solid rgb(76, 162, 249);
	   
	}
	QPushButton#pushButton_ok:pressed {
	       background-color: qlineargradient(spread:pad, x1:0, y1:0.994, x2:0, y2:0.0569545, stop:0.0340909 rgba(0, 170, 255, 255), stop:1 rgba(170, 214, 255, 255));
	    }


	/*QPushButton cancel*/

	QPushButton#pushButton_cancel {
	    color: rgb(33, 33, 33);
	    background-color: qlineargradient(spread:reflect, x1:0.0454545, y1:0, x2:0.006, y2:1, stop:0 rgba(235, 235, 235, 255), stop:0.801136 rgba(176, 176, 176, 255));
	    border: 1px solid rgb(180, 180, 180);
	    border-radius: 5px;
	       
	}
	QPushButton#pushButton_cancel:hover { 
	    background-color: qlineargradient(spread:reflect, x1:0.0454545, y1:0, x2:0.006, y2:1, stop:0 rgba(235, 235, 235, 255), stop:0.801136 rgba(210, 210, 210, 255));
	    border: 2px solid rgb(76, 162, 249);
	   
	}
	QPushButton#pushButton_cancel:pressed {
	       background-color:  qlineargradient(spread:reflect, x1:0.0454545, y1:0, x2:0.006, y2:1, stop:0 rgba(235, 235, 235, 255), stop:0.801136 rgba(230, 230, 230, 255));
	    }


	    
	/*QLabel*/
	QLabel#label_boldtext,#label_text{
	color: rgb(220, 220, 220);
	border: none;
	font-size: 16px;
	}
	QLabel#label_icon{
	
	}
	/*

	QMenu#tableMenu{
	width: 250px;
	height: 250px;
	background-color: rgb(33, 33, 33);
    color: white; 
    font-size: 16px;
    border: 1px solid rgb(50, 50, 50);
	}


	QMenu#tableMenu::item{
	color: white; 
	
	}
	QMenu#tableMenu::item:selected{	
	background-color: rgb(50, 50, 50);
    color: white; 
    font-size: 17px;
    border: 1px solid rgb(76, 162, 249);
    
	}
	*/
'''

light_theme ='''

	/*QToolTip*/
	QToolTip {
		background-color: rgb(240, 242, 245);
        color: rgb(33, 33, 33);
        font-size: 16px;
        border: 1px solid rgb(76, 162, 249);

	}
	/*QFrame*/

	QFrame#frame_menu_left,#frame_footer
	{
		background-color:rgb(33, 33, 33);
		
	}
	QFrame#frame_header,#frame_btn_window,#frame_title_bottom,#frame_top,#frame_title
	{
		border:None;
	}

	QFrame#frame_body ,#frame_title_bottom,#frame_title_app,#frame_logo,#frame_top
	{
		background-color:rgb(240, 242, 245);
		border: None;
	} 


	/*QLabel*/
	QLabel#label_timer_6,#label_timer_4
	{
		background-position: center;
		background-image: url(:/bold/iconapp/bold.40x40/4.png);
		background-repeat:None;
	}
	QFrame#frame_footer QLabel 
	{
	color: rgb(240, 240, 240);
	}
	/*QLineEdit*/

	QLineEdit
	{
		background-color:rgb(255, 255, 255);
		color:rgb(58, 57, 58);
		border:2px solid rgb(91, 152, 248);	
		border-radius: 5px;

	}

	QLineEdit:hover
	{	
		border:2px solid rgb(71, 124, 198);
	}
	QLineEdit:focus
	{	
		border: 2px solid rgb(71, 124, 198);
	}
	/*QPushButton*/
	QPushButton#pushButton_home, #pushButton_get_cmt, #pushButton_setting
	{
		background-color:rgb(33, 33, 33);
		color: rgba(255,255,255,210);
		border: None;
		border-radius: None;

	}
	QPushButton#pushButton_home:hover, #pushButton_get_cmt:hover, #pushButton_setting:hover
	{	
		background-color:rgb(65, 91, 116);
	}
	QPushButton#pushButton_home:pressed, #pushButton_get_cmt:pressed, #pushButton_setting:pressed
	{	
		background-color:rgb(96, 134, 171);
	}
	/*-----------*/

	QPushButton
	{
		background-color:rgb(75, 104, 133);
		color: rgba(255,255,255,210);
		border: None;
		border-radius: 5px;
		background-repeat: None;
		background-position:center;

	}

	QPushButton:hover
	{	
		background-color:rgb(65, 91, 116);
		border: 2px solid rgb(91, 152, 248);	
	}
	QPushButton:pressed
	{	
		background-color:  rgb(96, 134, 171);
	}

	/*-----------*/
	QPushButton#pushButton_home 
	{
		background-image: url(:/resource/iconapp/24x24/cil-moon.png);
	}


	QPushButton#pushButton_zoom_in 
	{
		background-image: url(:/bold/iconapp/bold.40x40/1.png);
	}
	QPushButton#pushButton_zoom_out
	{
		background-image: url(:/bold/iconapp/bold.40x40/2.png);
	}
	/*-----------*/
	QPushButton#pushButton_zoom_in,#pushButton_zoom_out,#pushButton_close
	{
		background-color:rgb(240, 242, 245);
		border: None;
		background-repeat: None;
		background-position:center;
		
	}
	QPushButton#pushButton_zoom_in:hover ,#pushButton_zoom_out:hover 
	{

		background-color: rgb(221, 232, 245);
		border: 1px solid rgb(71, 124, 198);
	}
	QPushButton#pushButton_zoom_in::pressed,#pushButton_zoom_out:pressed
	{		
		background-color:rgb(195, 212, 231);
	}

	QPushButton#pushButton_resize{
	background-image: url(:/16x16/iconapp/16x16/cil-size-grip.png);
	background-color:rgb(33, 33, 33);
	background-repeat:none;
	border-radius:-10px;
	}
	QPushButton#pushButton_resize:hover{
	border: none;
	}

	QPushButton#pushButton_close
	{
		background-image: url(:/bold/iconapp/bold.40x40/3.png);
	}

	QPushButton#pushButton_close:hover
	{
		background-color: rgb(255, 71, 35);
		background-image: url(:/16x16/iconapp/16x16/cil-x.png);
		
	}

	QPushButton#pushButton_close:pressed
	{
		background-color: rgb(252, 96, 66);
		
	}


	/*QSpinBox*/

	/*QGroupBox*/
	QGroupBox {
		color: rgb(255,255,255);
		border-radius: 5px;
		border: 1px solid rgb(91, 152, 248);	

	}
	/*QComboBox*/
	QComboBox,QSpinBox{
	color:rgb(255,255,255);
	background-color: rgb(75, 104, 133);
	border-radius: 5px;
	border: 1px solid rgb(48, 49, 52);
	padding-left:8px;
	}
	QComboBox::hover {
	background-color:rgb(65, 91, 116);
	border-color:rgb(96, 134, 171);
	}

	QComboBox::drop-down {
	    width: 30px;	
		background-image: url(:/16x16/iconapp/16x16/cil-arrow-bottom.png);
		background-repeat: None;
		background-position: center;

	}
	QComboBox QAbstractItemView
	{    
	    color: rgb(255,255,255);
		background-color:rgb(75, 104, 133);
	    selection-background-color: rgb(119, 155, 213);

	}
	/*QSpinBox*/

	/*QLabel*/
	QLabel
	{
		background:None;
		color:rgb(58, 57, 58);
	}
	/*QTextEdit*/
	QTextEdit {	
		color: rgb(58, 57, 58);
		border-radius: 5px;
		border: 1px solid rgb(91, 152, 248);
		background-color:rgb(255, 255, 255);
		padding-left: 5px;
	}
	/* QCheckbox,QRadioButton*/
	QCheckBox,QRadioButton
	{		
		color:rgb(58, 57, 58);
	   

	}
	QCheckBox::indicator,QRadioButton::indicator{
		color:rgb(91, 152, 248);
		border: 2px solid rgb(240, 242, 245);
		height: 20px;
		width:20px;
		border-radius:12px;
		background: rgb(44, 49, 60);
		
	}
	QCheckBox::indicator:hover,QRadioButton::indicator:hover{
		 border: 2px solid rgb(62, 106, 172);
		 border-radius: 10px;
	}
	QCheckBox::indicator:checked,QRadioButton::indicator:checked  {
	 	background: rgb(91, 152, 248);
	    border: 2px solid rgb(91, 152, 248);
		border-radius:12px;     
		background-image: url(:/resource/iconapp/24x24/cil-check-alt.png);
	}
	QCheckBox::indicator:unchecked,QRadioButton::indicator:unchecked{
	 	background: rgb(240, 242, 245);
	    border: 2px solid rgb(91, 152, 248);
		border-radius:12px;     

	}

	QCheckBox#checkBox_num:indicator {
		width: 33px; 
		height: 23px;
		border-radius:-12px;
		border:1px solid rgb(36,36,36);
		background-repeat:none;

	}

		/* SCROLL BARS*/
	QScrollBar:horizontal {
	    border: none;
	    background:rgb(230, 230, 230);
	    height: 8px;
	    margin: 0px 21px 0 21px;
		border-radius: 0px;
	}
	QScrollBar::handle:horizontal {
	    background: rgb(138, 180, 248);
	    min-width: 25px;
		border-radius: 3px
	}
	QScrollBar::add-line:horizontal {
	    border: none;
	    background:rgb(230, 230, 230);
		width: 20px;
		border-top-right-radius: 7px;
	    border-bottom-right-radius: 7px;
	    subcontrol-position: right;
	    subcontrol-origin: margin;
	}
	QScrollBar::sub-line:horizontal {
	    border: none;
	    background:rgb(230, 230, 230);
	    width: 20px;
		border-top-left-radius: 7px;
	    border-bottom-left-radius: 7px;
	    subcontrol-position: left;
	    subcontrol-origin: margin;
	}
	QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
	{
	     background: none;
	}
	QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
	{
	    background: none;
	}
	 QScrollBar:vertical {
		border: none;
	    background-color:rgb(230, 230, 230);
	    width: 8px;
	    margin: 10px 0px 0px 0px; /*top right*/
		border-radius: 0px;
	 }
	 QScrollBar::handle:vertical {	
		background-color:rgb(138, 180, 248);
	    min-height: 50px;
		border-radius: 3px
	 }
	 QScrollBar::add-line:vertical {
	    border: none;
	    background:rgb(230, 230, 230);
	    height: 20px;
		border-bottom-left-radius: 7px;
	    border-bottom-right-radius: 7px;
	    subcontrol-position: bottom;
	    subcontrol-origin: margin;
	 }
	 QScrollBar::sub-line:vertical {
		 border: none;
	     background:rgb(230, 230, 230);
	     height: 20px;
		 border-top-left-radius: 7px;
	     border-top-right-radius: 7px;
	     subcontrol-position: top;
	     subcontrol-origin: margin;
	 }
	 QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
	     background: none;
	 }

	 QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
	     background: none;
	 }

	/*QtableWidget*/
	QTableWidget {	
	gridline-color: rgb(84, 144, 232);
	background-color:rgb(255, 255, 255);
	border-radius: 5px;
	border:None;
	color: rgb(0,0,0);
	}
	
	QTableWidget::item:selected{
	background-color:rgb(231, 240, 253);
	color: rgb(0,0,0);
	}

	QTableWidget::horizontalHeader {	
	background-color: rgb(75, 104, 133);
	}
	QHeaderView::section:horizontal
	{
	background-color:  rgb(75, 104, 133);
	color :  rgb(255,255,255);

	}
	QHeaderView::section{
        border-style: none;
        border-bottom: 1px solid rgb(44, 49, 60);
        border-right: 1px solid rgb(231, 234, 237);
    }

    /*---------------------- Message Box ----------------------------*/
	/*QFrame*/
	QFrame#frame_msg_main {
	background-color:rgb(235, 235, 235);
	border: none;
	border-radius: 5px;
	}
	QFrame#frame_msg_header{
	background-color:qlineargradient(spread:reflect, x1:0.0454545, y1:0, x2:0, y2:1, stop:0 rgba(235, 235, 235, 255), stop:0.801136 rgba(200, 200, 200, 255));
	border-bottom: 1px solid rgb(180,180,180);
	border-radius: 5px;
	border-bottom-right-radius: -5px;
	border-bottom-left-radius: -5px;
	}
	/*QPushButton*/

	 /*QPushButton cancel*/
	QPushButton#pushButton_ok {
	    color: rgb(255, 255, 255);
	    background-color: qlineargradient(spread:pad, x1:0, y1:0.994, x2:0, y2:0.0569545, stop:0.0340909 rgba(0, 170, 255, 255), stop:1 rgba(170, 214, 255, 255));
	    border: 1px solid rgb(76, 162, 249);
	    border-radius: 5px;
	       
	}
	QPushButton#pushButton_ok:hover { 
	    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 170, 255, 255), stop:0.755682 rgba(171, 224, 255, 255));
	    border: 2px solid rgb(76, 162, 249);
	   
	}
	QPushButton#pushButton_ok:pressed {
	       background-color: qlineargradient(spread:pad, x1:0, y1:0.994, x2:0, y2:0.0569545, stop:0.0340909 rgba(0, 170, 255, 255), stop:1 rgba(170, 214, 255, 255));
	    }


	    /*QPushButton cancel*/
	QPushButton#pushButton_cancel {
	    color: rgb(33, 33, 33);
	    background-color: qlineargradient(spread:reflect, x1:0.0454545, y1:0, x2:0.006, y2:1, stop:0 rgba(235, 235, 235, 255), stop:0.801136 rgba(176, 176, 176, 255));
	    border: 1px solid rgb(180, 180, 180);
	    border-radius: 5px;
	       
	}
	QPushButton#pushButton_cancel:hover { 
	    background-color: qlineargradient(spread:reflect, x1:0.0454545, y1:0, x2:0.006, y2:1, stop:0 rgba(235, 235, 235, 255), stop:0.801136 rgba(210, 210, 210, 255));
	    border: 2px solid rgb(76, 162, 249);
	   
	}
	QPushButton#pushButton_cancel:pressed {
	       background-color:  qlineargradient(spread:reflect, x1:0.0454545, y1:0, x2:0.006, y2:1, stop:0 rgba(235, 235, 235, 255), stop:0.801136 rgba(230, 230, 230, 255));
	    }


	/*QLabel*/
	QLabel#label_boldtext,#label_text{
	color: rgb(34, 34, 34);
	border: none;
	font-size: 16px;
	}
	QLabel#label_icon{
	
	}
'''