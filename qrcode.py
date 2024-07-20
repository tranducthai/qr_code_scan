import cv2
qrc=cv2.QRCodeDetector()
vid=cv2.VideoCapture(0)
decoded_qr_data = {}
while True:
    ret,frame=vid.read()
    if ret:
        retval, decode_qr, point,_=qrc.detectAndDecodeMulti(frame)
        if retval:
          if decode_qr:  
            for i, (s, p) in enumerate(zip(decode_qr, point)):
                if s:
                    decoded_qr_data[i] = (s, p)
            for _, (s, p) in decoded_qr_data.items():
             cv2.putText(frame, s, (int(p[0][0]), int(p[0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
             frame = cv2.polylines(frame, [p.astype(int)], True, (0, 0, 255), 2)
          else: 
             decoded_qr_data.clear() 
             cv2.putText(frame, 'Cannot detect', (100,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        else: 
         decoded_qr_data.clear()    
        cv2.imshow('QrCode', frame)  
    if cv2.waitKey(1) & 0xFF==ord('q') :
        break
cv2.destroyAllWindows()       