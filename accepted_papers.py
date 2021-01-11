import openreview
import argparse
import json

def get_papers(client):
    """Get the accepted papers from OpenReview"""
    print ('Connected to ', client.baseurl)

    accepted_notes = client.get_notes(
        invitation='AKBC.ws/2020/Conference/Paper.*/-/Decision')

    papers = []
    for index, acc_note in enumerate(accepted_notes):
        ppr_number = str(acc_note.invitation.split('Paper')[1].split('/')[0])
        if acc_note.content['decision'] == 'Reject':
            continue
        blind_note = client.get_notes(invitation = 'AKBC.ws/2020/Conference/-/Blind_Submission', number = ppr_number)[0]
        paper = blind_note.content
        paper['forum_id'] = blind_note.id
        paper['UID'] = ppr_number
        author_emails = paper['authorids']
        if len(author_emails) != len(paper['authors']):
            print("!!!! => mismatch for " + blind_note.id)
        author_profiles = []
        for email in author_emails:
            try:
                author_profile = client.get_profile(email)
                if author_profile.active != True:
                    author_profile = ""
                else:
                    author_profile = author_profile.id
            except openreview.OpenReviewException as e:
                author_profile = ""
            author_profiles.append(author_profile)
        paper['author_profiles'] = author_profiles
        papers.append(blind_note.content)
    print('Accepted submissions: ', len(papers))
    return papers

def save_to_json(papers, ofile = "papers.json"):
    with open(ofile, 'w') as f:
        json.dump(papers, f, indent=2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download the AKBC proceedings')
    parser.add_argument('--username', required=True, help='OpenReview username')
    parser.add_argument('--password', required=True, help='OpenReview password')
    args = parser.parse_args()

    client = openreview.Client(baseurl='https://api.openreview.net', username=args.username, password=args.password)
    papers = get_papers(client)
    save_to_json(papers)
    
    