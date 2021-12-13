import dropbox
class TransferData: 
    def _init_ (self,accesstoken):
        self.accesstoken=accesstoken
    def uploadfile(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        f=open(filefrom,'rb')
        dbx.fileupload(f.read(),fileto)   
        
        
def main():
    accesstoken='sl.A-FQ6eE99Z5gHGh2Y4F7uyu-OJvFyL3BNINiHAEEvh_yxWZb4Eg_irTyK_UmhoxITikDjNiXDKGwd2q_VPM0ZeFdxBEg9Rjn6s4ATo9A9hPKcpfUDiSYbWhntBPXFMTXy_cjC5Q'
    transferData =TransferData(accesstoken)
    filefrom='C:/Users/Hp/Downloads/class97 coding/empty.txt'
    fileto='C:/Users/Hp/Dropbox'
    transferData.uploadfile (filefrom,fileto)
    print('file has been moved')      
    
main()    