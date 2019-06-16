###### EDIT ##################### 
#Directory with ui and resource files
RESOURCE_DIR = Designer
 
#Directory for compiled resources
COMPILED_DIR = CoverletterCreator/ui
 
#UI files to compile
UI_FILES = mainWindow.ui settings.ui progress.ui
#Qt resource files to compile
RESOURCES = CoverletterCreator.ui.resources.qrc 
 
#pyuic5 and pyrcc5 binaries
PYUIC = pyuic5
PYRCC = pyrcc5
 
#################################
# DO NOT EDIT FOLLOWING
 
COMPILED_UI = $(UI_FILES:%.ui=$(COMPILED_DIR)/%.py)
COMPILED_RESOURCES = $(RESOURCES:%.qrc=$(COMPILED_DIR)/%_rc.py)
 
all : resources ui 
 
resources : $(COMPILED_RESOURCES) 
 
ui : $(COMPILED_UI)
 
$(COMPILED_DIR)/%.py : $(RESOURCE_DIR)/%.ui
	$(PYUIC) $< -o $@
 
$(COMPILED_DIR)/%_rc.py : $(RESOURCE_DIR)/%.qrc
	$(PYRCC) $< -o $(COMPILED_DIR)/resources_rc.py
 
clean : 
	$(RM) $(COMPILED_UI) $(COMPILED_RESOURCES) $(COMPILED_UI:.py=.pyc) $(COMPILED_RESOURCES:.py=.pyc)  
