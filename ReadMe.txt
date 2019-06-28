To check the output of project follow below steps:

	1.Download complete AWS folder.
	2.In the AWS folder copy "local_host" folder in local machine.
	3.In the AWS folder copy "server_code" folder in AWS Ec3 instance.

Before recognition program:
	1.Run "1st_face_registration.py" file in local machine.
	2.Then Run "2nd_train_face_dataset.py" file in local machine.
	3.Copy "recognizer.yml" to "server_code" folder on AWS Ec3 instance.

On Server:
	1.After copy run the "predict_server.py" file on the AWS Ec3 instance.
	2.Then run "predict_server_upload.py" file on the AWS Ec3 instance.
	3.Ensure that both files are working properly on the AWS server and ports are listning.

Once ports are listning:
	1.Run the "3rd_predict_live.py" file on the local machine.

After successfull execution of above stepes you will get the output.
