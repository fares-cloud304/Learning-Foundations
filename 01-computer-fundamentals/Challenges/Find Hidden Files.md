:

# Challenge: Find Hidden Files


## Command Used


```bash
cd ~
ls -la
What I Found

The command showed these hidden files and directories in my home directory:

.bash_history
.bash_logout
.bashrc
.cache
.config
.motd_shown
.profile

ls -la shows hidden files because the -a option means all, including files beginning with ..

What I Learned

Linux treats files and directories whose names begin with . as hidden by default.

They commonly exist for configuration, user settings, application data, and shell settings.

Hidden does not mean encrypted or secret. It mainly keeps normal directory listings cleaner.

I also learned that hidden files can still be accessed normally if I know their names.