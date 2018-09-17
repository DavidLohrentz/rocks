# Save this Dockerfile in folder with rock_paper.py
# To create the image: docker build -t rocks .
# To start the container: docker run --rm -ti \
# -v /home/david/Documents/projects/rocks:/var/opt \
# -p 4000:80 rocks
#    or use bash start_rock.sh script

# Use an Alpine Python runtime
FROM python:3.7.0-alpine3.8

# Set the working directory to /var/opt
WORKDIR /var/opt

# Copy the current directory contents into the container at /var/opt
ADD . /var/opt

# Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

VOLUME /var/opt

# Run rock_paper.py when the container launches
CMD ["python", "rock_paper.py"]
