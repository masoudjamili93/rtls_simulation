python run_rtls_server.py &
python run_pitch_client.py &
sleep 30
pkill -f run_rtls_server.py &
pkill -f run_pitch_client.py &