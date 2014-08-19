export PATH=/Applications/Montage_v3.3/bin:$PATH
export PATH=/Applications/boost_1_55_0:$PATH
export PATH=/Applications/stinytim:$PATH

# Setting PATH for Python 2.7
PATH="//anaconda/bin/python:${PATH}"
export PATH

export PATH=/usr/local/bin:$PATH
alias mv="mv -i"
alias cp="cp -i"
alias rm="rm -i"
alias l="ls -F"	#	Works
alias ls="ls -F"
alias ll='ls -la'
alias la="ls -a"
alias cl="clear"
alias lh="ls -lrth"
alias pylab="ipython -pylab"
alias ..='cd ..'
alias ...='cd ../../'
alias ds9="/Applications/ds9.darwinmountainlion.7.2/ds9"
alias stiny1='/Applications/stinytim/stiny1'
alias stiny2='/Applications/stinytim/stiny2'

ur_setup() {
    eval `/Users/Laureth/.ureka/ur_setup -sh $*`
}
ur_forget() {
    eval `/Users/Laureth/.ureka/ur_forget -sh $*`
}
